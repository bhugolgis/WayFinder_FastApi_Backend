import asyncio
from sqlalchemy import select, func, extract, and_
from app.database import AsyncSessionLocal
from app.models.models import VisitorAnalysis

async def run():
    async with AsyncSessionLocal() as db:
        # Get first 10000 records
        subq = select(VisitorAnalysis).limit(10000).subquery()
        
        # Unique filter logic on these 10000
        # Wait, the frontend logic:
        # uniqueVisitorsMap = new Map();
        # records.forEach(r => { if (!uniqueVisitorsMap.has(r.Username)) uniqueVisitorsMap.set(r.Username, r) });
        # This is essentially: pick the row with the smallest ID for each username in the result set.
        
        ist_hour = extract('hour', func.timezone('Asia/Kolkata', func.timezone('UTC', subq.c.date_created)))
        
        # We need to simulate the unique map in SQL for the subq
        ui_sub = select(func.min(subq.c.id)).where(subq.c.Username != "").group_by(subq.c.Username)
        
        q = select(func.count(subq.c.id)).where(and_(subq.c.id.in_(ui_sub), ist_hour == 0))
        res = await db.execute(q)
        print(f"Unique visitors at 00:00 IST for FIRST 10,000 records: {res.scalar()}")
        
        # Try for first 20000
        subq2 = select(VisitorAnalysis).limit(20000).subquery()
        ui_sub2 = select(func.min(subq2.c.id)).where(subq2.c.Username != "").group_by(subq2.c.Username)
        res2 = await db.execute(select(func.count(subq2.c.id)).where(and_(subq2.c.id.in_(ui_sub2), extract('hour', func.timezone('Asia/Kolkata', func.timezone('UTC', subq2.c.date_created))) == 0)))
        print(f"Unique visitors at 00:00 IST for FIRST 20,000 records: {res2.scalar()}")

if __name__ == "__main__":
    asyncio.run(run())
