import httpx

# 🔴 Remove extra spaces in URL!
STATION_BASE_URL = "https://adminwayfinder.bhugolapps.com/items/Stations"

async def get_station_name_by_id(station_id: int) -> str | None:
    """
    Fetch station name by ID from external CMS API (async).
    """
    url = f"{STATION_BASE_URL}/{station_id}"
    params = {
        "fields": "Station_Name"
    }

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Directus returns data like: { "data": { "Station_Name": "..." } }
            station_name = data.get("data", {}).get("Station_Name")
            return station_name

        except httpx.HTTPStatusError as e:
            print(f"HTTP error fetching station {station_id}: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error fetching station {station_id}: {e}")
            return None