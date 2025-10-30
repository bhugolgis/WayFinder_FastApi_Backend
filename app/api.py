from fastapi import APIRouter, Depends, Query
from typing import Optional

from sqlalchemy import select
from app.journey_logic import plan_journey
from app.database import get_db
from app.models.journey_tracking import JourneyTracking
from app.models.models import Stations
from app.repository.poi_repository import get_poi_coordinates
from geopy.distance import geodesic
from sqlalchemy.ext.asyncio import AsyncSession  # ✅ Use AsyncSession

router = APIRouter()

@router.get("/journey")
async def journey_api(
    source_lat: Optional[float] = None,
    source_lng: Optional[float] = None,
    source_station_name: Optional[str] = None,
    destination_type: str = Query(..., regex="^(poi|metro_stn)$"),
    destination_value: str = Query(...),
    db: AsyncSession = Depends(get_db)  # ✅ AsyncSession
):
    result = await plan_journey(
        source_lat=source_lat,
        source_lng=source_lng,
        source_station_name=source_station_name,
        destination_type=destination_type,
        destination_value=destination_value,
    )

    tracking_data = {
        "source_station_name": source_station_name,
        "source_lat": source_lat,
        "source_lng": source_lng,
        "destination_type": destination_type,
        "destination_name": destination_value,
        "destination_station_name": None,
        "destination_lat": None,
        "destination_lng": None,
        "nearest_entry_gate": None,
        "nearest_exit_gate": None,
        "metro_route": None,
        "journey_steps": result.get("journey_array"),
        "distance_to_poi": None,
    }

    if destination_type == "poi":
        poi = await get_poi_coordinates(destination_value)
        if poi:
            tracking_data["destination_lat"] = float(poi.get("lat"))
            tracking_data["destination_lng"] = float(poi.get("lng"))
            tracking_data["destination_station_name"] = poi.get("station_name")
            if source_lat is not None and source_lng is not None:
                tracking_data["distance_to_poi"] = geodesic(
                    (source_lat, source_lng),
                    (poi["lat"], poi["lng"])
                ).meters

    else:
        stmt = select(Stations).where(Stations.Station_Name == destination_value)
        result_station = await db.execute(stmt)
        station = result_station.scalar_one_or_none()
        if station:
            tracking_data["destination_station_name"] = destination_value
            tracking_data["destination_lat"] = float(station.Station_Latitude)
            tracking_data["destination_lng"] = float(station.Station_Longitude)

    if result["status"] == "success":
        steps = result.get("journey_array", [])
        for step in steps:
            if step.get("title") == "Nearest Exit Gate":
                exit_gate_name = step.get("description")
                tracking_data["nearest_exit_gate"] = {
                    "gate_name": exit_gate_name,
                    "station": tracking_data["destination_station_name"]
                }
            elif step.get("title") == "Metro Route":
                tracking_data["metro_route"] = step.get("metro_stations")

    # ✅ Save to DB with await
    journey_record = JourneyTracking(**tracking_data)
    db.add(journey_record)
    await db.commit()
    await db.refresh(journey_record)

    return result