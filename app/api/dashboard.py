from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, desc, extract
from app.database import get_db
from app.models.models import VisitorAnalysis, Stations, Places
from datetime import datetime, timedelta
import pandas as pd
import io
from typing import Optional, List

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

# Filter logic replicated from frontend: Keep only the first record for each user


@router.get("/counts")
async def get_visitor_counts(
    station_id: Optional[int] = None,
    station_name: Optional[str] = None,
    place_id: Optional[int] = None,
    place_name: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    now = datetime.now()
    
    # helper for bounds
    def get_bounds(period: str):
        if period == "daily":
            # todayStart to todayEnd
            start = now.replace(hour=0, minute=0, second=0, microsecond=0)
            end = now
            prev_start = start - timedelta(days=1)
            prev_end = start - timedelta(microseconds=1)
        elif period == "weekly":
            # weekStart to now
            start = (now - timedelta(days=7)).replace(hour=0, minute=0, second=0, microsecond=0)
            end = now
            prev_start = (now - timedelta(days=14)).replace(hour=0, minute=0, second=0, microsecond=0)
            prev_end = start - timedelta(microseconds=1)
        elif period == "monthly":
            # monthStart to now
            start = (now - timedelta(days=30)).replace(hour=0, minute=0, second=0, microsecond=0)
            end = now
            prev_start = (now - timedelta(days=60)).replace(hour=0, minute=0, second=0, microsecond=0)
            prev_end = start - timedelta(microseconds=1)
        elif period == "yearly":
            # yearStart to now
            start = now.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            end = now
            prev_start = (start - timedelta(days=365)).replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            prev_end = start - timedelta(microseconds=1)
        return start, end, prev_start, prev_end

    async def get_period_count(period: str):
        start, end, prev_start, prev_end = get_bounds(period)
        
        # Helper to get unique IDs within a specific range
        def get_unique_ids_for_range(s, e):
            stmt = select(func.min(VisitorAnalysis.id)).where(and_(
                VisitorAnalysis.Username.isnot(None), 
                VisitorAnalysis.Username != "",
                VisitorAnalysis.date_created >= s,
                VisitorAnalysis.date_created <= e
            ))
            if station_id:
                stmt = stmt.where(VisitorAnalysis.Station == station_id)
            if station_name:
                stmt = stmt.where(VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
            if place_id:
                stmt = stmt.where(VisitorAnalysis.Place == place_id)
            if place_name:
                stmt = stmt.where(VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
            return stmt.group_by(VisitorAnalysis.Username)

        # Current period unique visitors
        curr_unique = get_unique_ids_for_range(start, end)
        curr_stmt = select(func.count(VisitorAnalysis.id)).where(VisitorAnalysis.id.in_(curr_unique))
        
        # Previous period for trend
        prev_unique = get_unique_ids_for_range(prev_start, prev_end)
        prev_stmt = select(func.count(VisitorAnalysis.id)).where(VisitorAnalysis.id.in_(prev_unique))
        
        curr_res = await db.execute(curr_stmt)
        prev_res = await db.execute(prev_stmt)
        
        curr_count = curr_res.scalar() or 0
        prev_count = prev_res.scalar() or 0
        
        trend = 0.0
        if prev_count > 0:
            trend = float(((curr_count - prev_count) / prev_count) * 100)
        elif curr_count > 0 and prev_count == 0:
            trend = 100.0
            
        labels = {
            "daily": "Last 24 Hours Visitors",
            "weekly": "Last 7 Days Visitors",
            "monthly": "Last 30 Days Visitors",
            "yearly": "Year To Date Visitors"
        }
        
        def format_date_range(p: str, s: datetime, e: datetime):
            if p == "daily":
                return f"{e.strftime('%b')} {e.day}"
            elif p == "yearly":
                return f"{s.strftime('%b')} {s.day}, {s.year}-{e.strftime('%b')} {e.day}"
            else:
                return f"{s.strftime('%b')} {s.day}-{e.strftime('%b')} {e.day}"
                
        return {
            "label": labels.get(period, ""),
            "dateRange": format_date_range(period, start, end),
            "value": curr_count, 
            "trend": float(f"{trend:.1f}")
        }

    return {
        "daily": await get_period_count("daily"),
        "weekly": await get_period_count("weekly"),
        "monthly": await get_period_count("monthly"),
        "yearly": await get_period_count("yearly")
    }

@router.get("/top-stations")
async def get_top_stations(
    station_id: Optional[int] = None,
    station_name: Optional[str] = None,
    place_id: Optional[int] = None,
    place_name: Optional[str] = None,
    from_date: Optional[str] = None, 
    to_date: Optional[str] = None,
    month: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    # Step 1: Define specific range conditions
    dt_from, dt_to = None, None
    if month:
        year, m = map(int, month.split("-"))
        dt_from = datetime(year, m, 1)
        if m == 12:
            dt_to = datetime(year + 1, 1, 1)
        else:
            dt_to = datetime(year, m + 1, 1)
    elif from_date and to_date:
        dt_from = datetime.fromisoformat(from_date)
        dt_to = datetime.fromisoformat(to_date)

    # Step 2: Calculate local UNIQUE visitors for this specific range
    range_unique_ids = (
        select(func.min(VisitorAnalysis.id))
        .where(and_(VisitorAnalysis.Username.isnot(None), VisitorAnalysis.Username != ""))
    )
    if dt_from:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created <= dt_to)
    if station_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station == station_id)
    if station_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place == place_id)
    if place_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
    
    range_unique_ids = range_unique_ids.group_by(VisitorAnalysis.Username).subquery()

    stmt = select(
        Stations.Station_Name,
        func.count(VisitorAnalysis.id).label("visits")
    ).join(VisitorAnalysis, VisitorAnalysis.Station == Stations.id)

    # Step 3: Filter results by the range-local unique IDs
    stmt = stmt.where(VisitorAnalysis.id.in_(select(range_unique_ids)))
    
    if station_id:
        stmt = stmt.where(VisitorAnalysis.Station == station_id)
    if station_name:
        stmt = stmt.where(VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        stmt = stmt.where(VisitorAnalysis.Place == place_id)
    if place_name:
        stmt = stmt.where(VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
    if dt_from:
        stmt = stmt.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        stmt = stmt.where(VisitorAnalysis.date_created <= dt_to)
        
    stmt = stmt.group_by(Stations.id, Stations.Station_Name).order_by(desc("visits")).limit(5)
    result = await db.execute(stmt)
    return [{"name": row[0], "visits": row[1]} for row in result.all()]

@router.get("/top-places")
async def get_top_places(
    station_id: Optional[int] = None,
    station_name: Optional[str] = None,
    place_id: Optional[int] = None,
    place_name: Optional[str] = None,
    from_date: Optional[str] = None, 
    to_date: Optional[str] = None,
    month: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    # Step 1: Define specific range conditions
    dt_from, dt_to = None, None
    if month:
        year, m = map(int, month.split("-"))
        dt_from = datetime(year, m, 1)
        if m == 12:
            dt_to = datetime(year + 1, 1, 1)
        else:
            dt_to = datetime(year, m + 1, 1)
    elif from_date and to_date:
        dt_from = datetime.fromisoformat(from_date)
        dt_to = datetime.fromisoformat(to_date)

    # Step 2: Calculate local UNIQUE visitors for this specific range
    range_unique_ids = (
        select(func.min(VisitorAnalysis.id))
        .where(and_(VisitorAnalysis.Username.isnot(None), VisitorAnalysis.Username != ""))
    )
    if dt_from:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created <= dt_to)
    if station_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station == station_id)
    if station_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place == place_id)
    if place_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
    
    range_unique_ids = range_unique_ids.group_by(VisitorAnalysis.Username).subquery()

    stmt = select(
        Places.Locality_Name,
        func.count(VisitorAnalysis.id).label("visits")
    ).join(VisitorAnalysis, VisitorAnalysis.Place == Places.id)

    # Step 3: Filter results by the range-local unique IDs
    stmt = stmt.where(VisitorAnalysis.id.in_(select(range_unique_ids)))
    
    if station_id:
        stmt = stmt.where(VisitorAnalysis.Station == station_id)
    if station_name:
        stmt = stmt.where(VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        stmt = stmt.where(VisitorAnalysis.Place == place_id)
    if place_name:
        stmt = stmt.where(VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
    if dt_from:
        stmt = stmt.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        stmt = stmt.where(VisitorAnalysis.date_created <= dt_to)
        
    stmt = stmt.group_by(Places.id, Places.Locality_Name).order_by(desc("visits")).limit(5)
    # Filter out null/empty names like frontend does
    stmt = stmt.where(Places.Locality_Name.isnot(None))
    
    result = await db.execute(stmt)
    return [{"name": row[0], "visits": row[1]} for row in result.all()]

@router.get("/time-trends")
async def get_time_trends(
    station_id: Optional[int] = None,
    station_name: Optional[str] = None,
    place_id: Optional[int] = None,
    place_name: Optional[str] = None,
    from_date: Optional[str] = None, 
    to_date: Optional[str] = None,
    month: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    # Step 1: Define time range based on inputs
    dt_from, dt_to = None, None
    if month:
        year, m = map(int, month.split("-"))
        dt_from = datetime(year, m, 1)
        # End of the month
        if m == 12:
            dt_to = datetime(year + 1, 1, 1)
        else:
            dt_to = datetime(year, m + 1, 1)
    elif from_date and to_date:
        dt_from = datetime.fromisoformat(from_date)
        dt_to = datetime.fromisoformat(to_date)

    # Step 2: Calculate local UNIQUE visitors for the requested range to include returning users
    # This matches the expected "Unique Visitors in [Period]" behavior.
    range_unique_ids = (
        select(func.min(VisitorAnalysis.id))
        .where(and_(VisitorAnalysis.Username.isnot(None), VisitorAnalysis.Username != ""))
    )
    if dt_from:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created <= dt_to)
    if station_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station == station_id)
    if station_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place == place_id)
    if place_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
    
    range_unique_ids = range_unique_ids.group_by(VisitorAnalysis.Username).subquery()

    # Step 3: Build the main trend query using these range-local IDs
    # Since DB apparently returns UTC hours when rawly extracted, we manually add IST offset (5.5 hours).
    ist_time = VisitorAnalysis.date_created + timedelta(hours=5, minutes=30)
    ist_hour = extract('hour', ist_time).label("hour")

    stmt = select(
        ist_hour,
        func.count(VisitorAnalysis.id)
    ).join(Stations, VisitorAnalysis.Station == Stations.id)

    # Filter to only the unique IDs found in this range
    stmt = stmt.where(VisitorAnalysis.id.in_(select(range_unique_ids)))
    
    if station_id:
        stmt = stmt.where(VisitorAnalysis.Station == station_id)
    if station_name:
        stmt = stmt.where(VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        stmt = stmt.where(VisitorAnalysis.Place == place_id)
    if place_name:
        stmt = stmt.where(VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))

    if dt_from:
        stmt = stmt.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        stmt = stmt.where(VisitorAnalysis.date_created <= dt_to)
        
    stmt = stmt.group_by("hour").order_by("hour")
    result = await db.execute(stmt)
    rows = result.all()
    
    trend_data = {f"{h}:00": {"name": f"{h}:00", "count": 0} for h in range(24)}
    for row in rows:
        h_val = row[0]
        if h_val is None: continue
        hour_key = f"{int(h_val)}:00"
        trend_data[hour_key]["count"] = row[1]
        
    return sorted(list(trend_data.values()), key=lambda x: int(x['name'].split(':')[0]))

async def get_time_trends_matrix(
    from_date: Optional[str] = None, 
    to_date: Optional[str] = None,
    month: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    dt_from, dt_to = None, None
    if month:
        year, m = map(int, month.split("-"))
        dt_from = datetime(year, m, 1)
        if m == 12:
            dt_to = datetime(year + 1, 1, 1)
        else:
            dt_to = datetime(year, m + 1, 1)
    elif from_date and to_date:
        dt_from = datetime.fromisoformat(from_date)
        dt_to = datetime.fromisoformat(to_date)

    range_unique_ids = (
        select(func.min(VisitorAnalysis.id))
        .where(and_(VisitorAnalysis.Username.isnot(None), VisitorAnalysis.Username != ""))
    )
    if dt_from:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created <= dt_to)
    
    range_unique_ids = range_unique_ids.group_by(VisitorAnalysis.Username).subquery()

    ist_time = VisitorAnalysis.date_created + timedelta(hours=5, minutes=30)
    ist_hour = extract('hour', ist_time).label("hour")

    stmt = select(
        ist_hour,
        Stations.Station_Name,
        func.count(VisitorAnalysis.id)
    ).join(Stations, VisitorAnalysis.Station == Stations.id)

    stmt = stmt.where(VisitorAnalysis.id.in_(select(range_unique_ids)))
    
    if dt_from:
        stmt = stmt.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        stmt = stmt.where(VisitorAnalysis.date_created <= dt_to)
        
    stmt = stmt.group_by("hour", Stations.Station_Name)
    result = await db.execute(stmt)
    rows = result.all()
    
    all_stations = list(set(r[1] for r in rows if r[1] is not None))
    all_stations.sort()
    
    trend_data = {f"{h}:00": {"name": f"{h}:00", **{st: "" for st in all_stations}} for h in range(24)}
    
    for row in rows:
        h_val = row[0]
        st_name = row[1]
        count = row[2]
        if h_val is None or st_name is None: continue
        hour_key = f"{int(h_val)}:00"
        trend_data[hour_key][st_name] = count
        
    return sorted(list(trend_data.values()), key=lambda x: int(x['name'].split(':')[0]))

@router.get("/station-visits")
async def get_all_station_visits(
    station_id: Optional[int] = None,
    station_name: Optional[str] = None,
    place_id: Optional[int] = None,
    place_name: Optional[str] = None,
    from_date: Optional[str] = None, 
    to_date: Optional[str] = None,
    month: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    # Step 1: Define specific range conditions
    dt_from, dt_to = None, None
    if month:
        year, m = map(int, month.split("-"))
        dt_from = datetime(year, m, 1)
        if m == 12:
            dt_to = datetime(year + 1, 1, 1)
        else:
            dt_to = datetime(year, m + 1, 1)
    elif from_date and to_date:
        dt_from = datetime.fromisoformat(from_date)
        dt_to = datetime.fromisoformat(to_date)

    # Step 2: Calculate local UNIQUE visitors for this specific range
    range_unique_ids = (
        select(func.min(VisitorAnalysis.id))
        .where(and_(VisitorAnalysis.Username.isnot(None), VisitorAnalysis.Username != ""))
    )
    if dt_from:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created <= dt_to)
    if station_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station == station_id)
    if station_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place == place_id)
    if place_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
    
    range_unique_ids = range_unique_ids.group_by(VisitorAnalysis.Username).subquery()

    # Step 3: Build a condition to only count unique visits within the join
    count_condition = and_(
        VisitorAnalysis.Station == Stations.id,
        VisitorAnalysis.id.in_(select(range_unique_ids))
    )

    if station_id:
        count_condition = and_(count_condition, VisitorAnalysis.Station == station_id)
    if station_name:
        count_condition = and_(count_condition, VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        count_condition = and_(count_condition, VisitorAnalysis.Place == place_id)
    if place_name:
        count_condition = and_(count_condition, VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
    if dt_from:
        count_condition = and_(count_condition, VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        count_condition = and_(count_condition, VisitorAnalysis.date_created <= dt_to)

    # Step 4: Perform inner join so stations with 0 visits are excluded
    stmt = select(
        Stations.Station_Name,
        func.count(VisitorAnalysis.id).label("visits")
    ).join(VisitorAnalysis, count_condition).group_by(Stations.id, Stations.Station_Name).order_by(desc("visits")).having(func.count(VisitorAnalysis.id) > 0)

    result = await db.execute(stmt)
    return [{"name": row[0], "visits": row[1]} for row in result.all()]

@router.get("/place-visits")
async def get_all_places_visits(
    station_id: Optional[int] = None,
    station_name: Optional[str] = None,
    place_id: Optional[int] = None,
    place_name: Optional[str] = None,
    from_date: Optional[str] = None, 
    to_date: Optional[str] = None,
    month: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    # Step 1: Define specific range conditions
    dt_from, dt_to = None, None
    if month:
        year, m = map(int, month.split("-"))
        dt_from = datetime(year, m, 1)
        if m == 12:
            dt_to = datetime(year + 1, 1, 1)
        else:
            dt_to = datetime(year, m + 1, 1)
    elif from_date and to_date:
        dt_from = datetime.fromisoformat(from_date)
        dt_to = datetime.fromisoformat(to_date)

    # Step 2: Calculate local UNIQUE visitors for this specific range
    range_unique_ids = (
        select(func.min(VisitorAnalysis.id))
        .where(and_(VisitorAnalysis.Username.isnot(None), VisitorAnalysis.Username != ""))
    )
    if dt_from:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created <= dt_to)
    if station_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station == station_id)
    if station_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place == place_id)
    if place_name:
        range_unique_ids = range_unique_ids.where(VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
    
    range_unique_ids = range_unique_ids.group_by(VisitorAnalysis.Username).subquery()

    # Step 3: Build a condition to only count unique visits within the join
    count_condition = and_(
        VisitorAnalysis.Place == Places.id,
        VisitorAnalysis.id.in_(select(range_unique_ids))
    )

    if station_id:
        count_condition = and_(count_condition, VisitorAnalysis.Station == station_id)
    if station_name:
        count_condition = and_(count_condition, VisitorAnalysis.Station.in_(select(Stations.id).where(Stations.Station_Name == station_name)))
    if place_id:
        count_condition = and_(count_condition, VisitorAnalysis.Place == place_id)
    if place_name:
        count_condition = and_(count_condition, VisitorAnalysis.Place.in_(select(Places.id).where(Places.Locality_Name == place_name)))
    if dt_from:
        count_condition = and_(count_condition, VisitorAnalysis.date_created >= dt_from)
    if dt_to:
        count_condition = and_(count_condition, VisitorAnalysis.date_created <= dt_to)

    # Step 4: Perform inner join so places with 0 visits are excluded
    stmt = select(
        Places.Locality_Name,
        func.count(VisitorAnalysis.id).label("visits")
    ).join(VisitorAnalysis, count_condition).group_by(Places.id, Places.Locality_Name).order_by(desc("visits")).having(func.count(VisitorAnalysis.id) > 0)

    result = await db.execute(stmt)
    return [{"name": row[0], "visits": row[1]} for row in result.all() if row[0] is not None]

@router.get("/export")
async def export_data(
    format: str = "Excel",
    selected: Optional[str] = None,
    from_date: Optional[str] = None,
    to_date: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    export_format = format
    selected_list = [s.strip() for s in selected.split(",")] if selected else []
    
    output = io.BytesIO()
    
    if export_format == "Excel":
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            has_sheets = False
            
            sl = [s.lower() for s in selected_list]
            is_all = any("all" in s for s in sl) or "all-data" in sl
            is_station = not is_all and ("station-wise" in sl or any("station" in s and "time" not in s for s in sl))
            is_place = not is_all and ("place-wise" in sl or any("place" in s for s in sl))
            is_time = not is_all and ("time-trend" in sl or any("time" in s for s in sl))
            is_month = not is_all and ("monthly-trend" in sl or any("month" in s for s in sl))
            
            # Ensure custom 1-row summary ONLY displays if Station-wise or All Data is selected
            if is_station or is_all:
                try:
                    dt_from, dt_to = None, None
                    if from_date and to_date:
                        dt_from = datetime.fromisoformat(from_date)
                        dt_to = datetime.fromisoformat(to_date)
                        date_range_str = f"{from_date} to {to_date}"
                    elif from_date:
                        dt_from = datetime.fromisoformat(from_date)
                        date_range_str = f"From {from_date}"
                    elif to_date:
                        dt_to = datetime.fromisoformat(to_date)
                        date_range_str = f"Until {to_date}"
                    else:
                        date_range_str = "All Time"
    
                    range_unique_ids = select(func.min(VisitorAnalysis.id)).where(and_(VisitorAnalysis.Username.isnot(None), VisitorAnalysis.Username != ""))
                    if dt_from: range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created >= dt_from)
                    if dt_to: range_unique_ids = range_unique_ids.where(VisitorAnalysis.date_created <= dt_to)
                    
                    range_unique_ids = range_unique_ids.group_by(VisitorAnalysis.Username).subquery()
                    
                    # 1. Total Visitors
                    stmt_v = select(func.count(VisitorAnalysis.id)).where(VisitorAnalysis.id.in_(select(range_unique_ids)))
                    if dt_from: stmt_v = stmt_v.where(VisitorAnalysis.date_created >= dt_from)
                    if dt_to: stmt_v = stmt_v.where(VisitorAnalysis.date_created <= dt_to)
                    tv = (await db.execute(stmt_v)).scalar() or 0
                    
                    # 2. Total Stations Count
                    stmt_s = select(func.count(VisitorAnalysis.id)).join(Stations, VisitorAnalysis.Station == Stations.id).where(VisitorAnalysis.id.in_(select(range_unique_ids)))
                    if dt_from: stmt_s = stmt_s.where(VisitorAnalysis.date_created >= dt_from)
                    if dt_to: stmt_s = stmt_s.where(VisitorAnalysis.date_created <= dt_to)
                    ts = (await db.execute(stmt_s)).scalar() or 0
                    
                    # 3. Total Places Count
                    stmt_p = select(func.count(VisitorAnalysis.id)).join(Places, VisitorAnalysis.Place == Places.id).where(and_(VisitorAnalysis.id.in_(select(range_unique_ids)), Places.Locality_Name.isnot(None)))
                    if dt_from: stmt_p = stmt_p.where(VisitorAnalysis.date_created >= dt_from)
                    if dt_to: stmt_p = stmt_p.where(VisitorAnalysis.date_created <= dt_to)
                    tp = (await db.execute(stmt_p)).scalar() or 0
    
                    summary_rows = [{
                        "Total Visitors": tv,
                        "Date Range": date_range_str,
                        "Total Stations Count": ts,
                        "Total Places Count": tp
                    }]
                    df_summary = pd.DataFrame(summary_rows)
                    df_summary.to_excel(writer, sheet_name="Summary", index=False)
                    has_sheets = True
                except Exception as e:
                    pass
                
            if is_station:
                res = await get_all_station_visits(from_date=from_date, to_date=to_date, db=db)
                df = pd.DataFrame(res).rename(columns={"name": "Station", "visits": "Visitors"})
                if not df.empty:
                    df.loc[len(df)] = ["Total", df["Visitors"].sum()]
                df.to_excel(writer, sheet_name="Station-wise Counts", index=False)
                has_sheets = True
                
            if is_place:
                res = await get_all_places_visits(from_date=from_date, to_date=to_date, db=db) 
                df = pd.DataFrame(res).rename(columns={"name": "Place", "visits": "Visitors"})
                if not df.empty:
                    df.loc[len(df)] = ["Total", df["Visitors"].sum()]
                df.to_excel(writer, sheet_name="Place-wise Counts", index=False)
                has_sheets = True
                
            if is_time:
                res = await get_time_trends_matrix(from_date=from_date, to_date=to_date, db=db)
                df = pd.DataFrame(res)
                # Ensure no custom "Total" row modifies the 2D layout. The "count" column logic doesn't apply here.
                df.to_excel(writer, sheet_name="Time Trend by Station", index=False)
                has_sheets = True
                
            if is_month:
                # Custom logic for Jan-Aug 2025 as requested
                # Re-using the matrix layout for monthly tabs
                for m_idx in range(1, 9): # Jan to Aug
                    month_name = datetime(2025, m_idx, 1).strftime("%b")
                    res = await get_time_trends_matrix(month=f"2025-{m_idx:02d}", db=db)
                    df = pd.DataFrame(res)
                    df.to_excel(writer, sheet_name=month_name, index=False)
                has_sheets = True
                    
            if is_all:
                # This usually combines several sheets
                s_res = await get_all_station_visits(from_date=from_date, to_date=to_date, db=db)
                s_df = pd.DataFrame(s_res).rename(columns={"name": "Station", "visits": "Visitors"})
                if not s_df.empty:
                    s_df.loc[len(s_df)] = ["Total", s_df["Visitors"].sum()]
                s_df.to_excel(writer, sheet_name="All Stations", index=False)
                
                p_res = await get_all_places_visits(from_date=from_date, to_date=to_date, db=db)
                p_df = pd.DataFrame(p_res).rename(columns={"name": "Place", "visits": "Visitors"})
                if not p_df.empty:
                    p_df.loc[len(p_df)] = ["Total", p_df["Visitors"].sum()]
                p_df.to_excel(writer, sheet_name="All Places", index=False)
                
                t_res = await get_time_trends_matrix(from_date=from_date, to_date=to_date, db=db)
                t_df = pd.DataFrame(t_res)
                t_df.to_excel(writer, sheet_name="Time Trend", index=False)
                has_sheets = True
                
            if not has_sheets:
                pd.DataFrame({"Message": ["No data matched selected option"]}).to_excel(writer, sheet_name="No Data", index=False)

        output.seek(0)
        headers = {
            'Content-Disposition': f'attachment; filename="visitor_dashboard_report_{datetime.now().strftime("%d-%m-%Y")}.xlsx"'
        }
        return StreamingResponse(output, headers=headers, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    else: # CSV - usually just the first requested or a combined one
        # For CSV simplified to first selected
        if any("station" in s.lower() for s in selected_list) or "station-wise" in selected_list:
            res = await get_all_station_visits(from_date=from_date, to_date=to_date, db=db)
            df = pd.DataFrame(res)
        elif any("place" in s.lower() for s in selected_list) or "place-wise" in selected_list:
            res = await get_all_places_visits(from_date=from_date, to_date=to_date, db=db)
            df = pd.DataFrame(res)
        else:
            df = pd.DataFrame({"message": ["CSV export not fully implemented for combined data or selection"]})
            
        csv_data = df.to_csv(index=False)
        return StreamingResponse(
            io.StringIO(csv_data),
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename=export.csv"}
        )
