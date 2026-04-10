import asyncio
import sys
from sqlalchemy import text
from app.database import AsyncSessionLocal

async def main():
    async with AsyncSessionLocal() as session:
        # Get latest entries
        result = await session.execute(text("SELECT id, \"date_created\" FROM \"VisitorAnalysis\" ORDER BY id DESC LIMIT 5"))
        print("LATEST:")
        for row in result.all():
            print(row)
            
        print("\nRAW HOURS:")
        res_raw = await session.execute(text("SELECT EXTRACT(HOUR FROM date_created) as h, COUNT(*) from \"VisitorAnalysis\" GROUP BY h ORDER BY h"))
        for row in res_raw.all():
            print(f"Hour {row[0]}: {row[1]}")

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
