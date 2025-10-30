import httpx

BASE_URL = "https://adminwayfinder.bhugolapps.com/items/Places"

async def get_poi_coordinates(locality_name: str):
    params = {
        "filter[Locality_Name][_eq]": locality_name,
        "fields": "Latitude,Longitude,Locality_Name, Station, Distance_From_Nearest_Gate, Nearest_Gates"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

    pois = data.get("data", [])

    print("pois_data: ", pois)
    if pois:
        return {
            "lat": pois[0]["Latitude"],
            "lng": pois[0]["Longitude"],
            "name": pois[0]["Locality_Name"],
            "station_id": pois[0]["Station"],
            "distance_from_nearest_gate": pois[0]["Distance_From_Nearest_Gate"],
            "nearest_gate": pois[0]["Nearest_Gates"]
        }
    else:
        return None
