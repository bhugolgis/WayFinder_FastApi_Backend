# test_db.py
import asyncio
import asyncpg

async def test():
    conn = await asyncpg.connect(
        host="134.209.148.225",
        port=5432,
        user="postgres",
        password="|Z851f3V0@_u",
        database="mmrcl_line3"
    )
    print("✅ Connected successfully!")
    await conn.close()

asyncio.run(test())