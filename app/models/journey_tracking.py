from sqlalchemy import Column, Integer, String, Float, JSON, DateTime
from sqlalchemy.sql import func
from app.database import Base


class JourneyTracking(Base):
    __tablename__ = "journey_tracking"

    id = Column(Integer, primary_key=True, index=True)
    
    # Source info
    source_station_name = Column(String, nullable=True)
    source_lat = Column(Float, nullable=True)
    source_lng = Column(Float, nullable=True)
    
    # Destination info
    destination_type = Column(String, nullable=False)  # "poi" or "metro_stn"
    destination_name = Column(String, nullable=False)
    destination_station_name = Column(String, nullable=True)
    destination_lat = Column(Float, nullable=True)
    destination_lng = Column(Float, nullable=True)

    # Journey details
    nearest_entry_gate = Column(JSON, nullable=True)  # {"gate_name": "B1", "station": "..."}
    nearest_exit_gate = Column(JSON, nullable=True)   # {"gate_name": "A1", "station": "..."}
    metro_route = Column(JSON, nullable=True)         # List of stations
    journey_steps = Column(JSON, nullable=True)       # Full journey array for reference
    
    # Distances
    distance_to_poi = Column(Float, nullable=True)    # meters

    created_at = Column(DateTime(timezone=True), server_default=func.now())
