from fastapi import Depends, FastAPI, Query, status, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from app.api import router as journey_router
from app.database import get_db
from app.models.models import TestPlaces
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update

app = FastAPI(title="Metro Journey Planner")

# ✅ Allow ALL origins (for development or public API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://wayfinder.bhugolapps.com", "http://10.202.100.187:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#checking trailing spaces

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "failed",
            "message": exc.detail,
            "journey_array": []
        }
    )

app.include_router(journey_router, prefix="/api")


@app.get("/journey-points")
def get_journey(
    location: str = Query(..., description="User's location"),
    poi: str = Query(..., description="Place of interest")
):
    journey_data = [
        {
            "title": f"Visit {poi} near {location}",
            "description": f"A great journey to the best {poi}s from {location}.",
            "metro_stations": {
                "no_of_stops": 5,
                "time": "25 mins",
                "stations": ["Station SEEPZ", "Station MIDC Andheri", "Station Marol Naka", "Station T2", "Station Sahar Road"]
            }
        }
    ]

    return JSONResponse(content={
        "message": "Journey recommendation fetched successfully.",
        "journey_array": journey_data
    })


@app.post("/update-all-type-of-lo", status_code=status.HTTP_200_OK)
async def update_all_type_of_lo(
    new_value: str = "TestValue",
    db: AsyncSession = Depends(get_db)
):
    try:
        stmt = update(TestPlaces).values(Type_of_Lo=new_value)
        result = await db.execute(stmt)
        await db.commit()
        return {
            "message": f"Successfully updated {result.rowcount} records",
            "new_value": new_value
        }
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )