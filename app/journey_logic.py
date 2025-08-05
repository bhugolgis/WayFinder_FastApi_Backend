from typing import List, Dict, Optional
from geopy.distance import geodesic
# from app.data import station_coords, poi_coords, entry_gates
from app.data import station_coords, entry_gates, stations_data
from fastapi import HTTPException
from app.repository.poi_repository import get_poi_coordinates
from app.repository.station_repository import get_station_name_by_id

async def plan_journey(
    source_lat: Optional[float],
    source_lng: Optional[float],
    source_station_name: Optional[str],
    destination_type: str,
    destination_value: str
):
    journey_steps = []
    # print("source_station_name: ", source_station_name)


    if source_station_name == destination_value:
        return {
            "status": "failed",
            "message": f"Source location and destination cannot be same",
            "journey_array": []
        }

    # Step 1: Get source coordinates
    station_names = [name for name, _ in station_coords]
    if source_station_name:
        is_source_metro_station = True
    else:
        is_source_metro_station = False


    if source_station_name:
        if source_station_name not in station_names:
            raise HTTPException(status_code=404, detail="Source station not found")

        source_coords = next((coord for name, coord in station_coords if name == source_station_name), None)
        # print("source_coords: ",source_coords)
    elif source_lat and source_lng:
        source_coords = (source_lat, source_lng)
    else:
        raise HTTPException(status_code=400, detail="Either source station name or lat/lng is required")

    # Step 2: Get destination coordinates
    if destination_type == "poi":
        poi = await get_poi_coordinates(destination_value)
        if not poi:
            raise HTTPException(status_code=404, detail="POI not found")
        destination_coords = (poi["lat"], poi["lng"])
        # print("destination_coords: ", destination_coords)
        
        is_destination_poi = True
        station_name_of_poi =  get_station_name_by_id(poi["station_id"])
        print("station_name_of_poi: ", station_name_of_poi)
        poi["station_name"] = station_name_of_poi
        print("poi_data: ", poi)
        
    elif destination_type == "metro_stn":
        if destination_value not in station_names:
            raise HTTPException(status_code=404, detail="Destination station not found")
        destination_coords = next((coord for name, coord in station_coords if name == destination_value), None)
        # print("destination_coords: ", destination_coords)
        is_destination_poi = False
    else:
        raise HTTPException(status_code=400, detail="Invalid destination type")

    # Step 3: Check if POI is within 1500m radius of source
    if is_destination_poi:
        dist_to_poi = geodesic(source_coords, destination_coords).meters
        # print("dist_to_poi: ", dist_to_poi)
        if dist_to_poi < 1500:
            return {
                "status": "failed",
                "message": f"The POI '{destination_value}' is just {int(dist_to_poi)} meters away. You can walk directly.",
                "journey_array": []
            }

    # Step 4: Find nearest entry gate within 2 km
    gates_within_2km = []
    for gate in entry_gates:
        gate_coords = (gate["lat"], gate["lng"])
        dist = geodesic(source_coords, gate_coords).meters
        if dist <= 2000:
            gates_within_2km.append((dist, gate))
    
    # print("gates_within_2km: ", gates_within_2km)
    
    if not gates_within_2km:
        return {
            "status": "failed",
            "message": "No metro entry gates found within 2 km radius. Please move closer to a metro station.",
            "journey_array": []
        }

    # Step 5: Get nearest entry gate
    nearest_gate = min(gates_within_2km, key=lambda x: x[0])[1]
    print("nearest_gate:", nearest_gate)
    start_metro_stn = nearest_gate["station"]
    print("start_metro_stn: ", start_metro_stn)

    # Step 6: If POI destination, check if it's at the same station as nearest entry gate
    if is_destination_poi and poi["name"] == start_metro_stn:
        return {
            "status": "failed",
            "message": f"The POI '{destination_value}' is at the same station as '{start_metro_stn}'. No need to use the metro.",
            "journey_array": []
        }

    # Step 7: Get the end metro station (based on POI or destination metro station)
    end_metro_stn = destination_value if not is_destination_poi else poi["station_name"]
    print("end_metro_stn: ", end_metro_stn)

    # Step 8: Generate metro route (logic for getting stations between start and end metro stations)
    metro_route = get_station_path(start_metro_stn, end_metro_stn)
    print("metro_route", metro_route)

    # Step 9: Construct the journey array
    if not is_source_metro_station:
        journey_steps.append({
            "step": 1,
            "title": "Nearest Entry Gate",
            "description": f'Gate {nearest_gate["gate_name"]} - {start_metro_stn}'
        })

    journey_steps.append({
        "step": 2,
        "title": "Metro Route",
        "description": f"{start_metro_stn} -> {end_metro_stn}",
        "metro_stations": metro_route
    })

    if is_destination_poi:
        journey_steps.append({
            "step": 3,
            "title": "Nearest Exit Gate",
            "description": poi["nearest_gate"]
            # "description": f"Gate {poi["nearest_gate"]} - {end_metro_stn}",
        })
        journey_steps.append({
            "step": 4,
            "title": "Distance",
            "description": poi["distance_from_nearest_gate"]
            # "description": f"29 meters"
        })
        journey_steps.append({
            "step": 5,
            "title": "Destination",
            "description": destination_value
        })
    else:
        journey_steps.append({
            "step": 5,
            "title": "Destination",
            "description": destination_value
        })

    return {
        "status": "success",
        "message": "Journey plan ready.",
        "journey_array": journey_steps
    }

def get_station_path(start: str, end: str) -> List[str]:
    # Sort stations by Display_Order descending
    sorted_stations = sorted(stations_data, key=lambda x: x["Display_Order"], reverse=True)
    # print("sorted_stations: ", sorted_stations)
    
    # Build a simple list of station names
    station_names = [station["Station_Name"] for station in sorted_stations]
    # print("station_names: ", station_names)
    print("start and end: ", start, end)

    try:
        print("brfore try")
        start_idx = station_names.index(start)
        print("hello")
        end_idx = station_names.index(end)
        print("start_idx, end_idx: ", start_idx, end_idx)
    except ValueError:
        return []  # One or both stations not found

    # Return path in correct direction
    if start_idx <= end_idx:
        return station_names[start_idx:end_idx + 1]
    else:
        return station_names[end_idx:start_idx + 1][::-1]
