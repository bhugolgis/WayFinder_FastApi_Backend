from fastapi import FastAPI, Query
from typing import List, Optional
from fastapi.responses import JSONResponse
from app.api import router as journey_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Metro Journey Planner")

app.include_router(journey_router, prefix="/api")

# List of allowed origins (frontend URLs, etc.)
origins = [
    "http://10.202.100.207:3000/",
    "http://localhost:3000",  # React/Vue dev server
    "https://wayfinder.bhugolapps.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Allows these origins
    allow_credentials=True,
    allow_methods=["*"],              # Allows all HTTP methods: GET, POST, PUT, etc.
    allow_headers=["*"],              # Allows all headers
)

@app.get("/journey-points")
def get_journey(
    location: str = Query(..., description="User's location"),
    poi: str = Query(..., description="Place of interest")
):
    # Sample static response — logic/db to be added later
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