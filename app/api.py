from fastapi import APIRouter, Query
from typing import Optional
from app.journey_logic import plan_journey

router = APIRouter()

@router.get("/journey")
async def journey_api(
    source_lat: Optional[float] = None,
    source_lng: Optional[float] = None,
    source_station_name: Optional[str] = None,
    destination_type: str = Query(..., regex="^(poi|metro_stn)$"),
    destination_value: str = Query(...),
):
    return await plan_journey(
        source_lat=source_lat,
        source_lng=source_lng,
        source_station_name=source_station_name,
        destination_type=destination_type,
        destination_value=destination_value,
    )
