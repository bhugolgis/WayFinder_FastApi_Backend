import httpx
import requests

STATION_BASE_URL = "https://adminwayfinder.bhugolapps.com/items/Stations"

def get_station_name_by_id(station_id: int):
    url = f"{STATION_BASE_URL}/{station_id}"
    params = {
        "fields": "Station_Name"
    }
    resp = requests.get(url, params=params, timeout=5)
    resp.raise_for_status()
    print(resp.json()["data"].get("Station_Name"))
    return resp.json()["data"].get("Station_Name")

    # async with httpx.AsyncClient() as client:
    #     response = await client.get(url, params=params)
    #     print(f"Status code: {response.status_code}")  # Debug: Print status code
    #     print(f"Raw response text: {response.text}")   # Debug: Print raw response body
    #     response.raise_for_status()
    #     data = response.json()
    #     print(f"Parsed JSON data: {data}")             # Debug: Print parsed JSON
    
    # station_name = data.get("data", {}).get("Station_Name")
    # return {"station_name": station_name}


# import requests
 
# url = "https://adminwayfinder.bhugolapps.com/items/Stations/11"
# params = {"fields": "Station_Name"}
 
# resp = requests.get(url, params=params, timeout=5)
# resp.raise_for_status()
 
# print(resp.json()["data"].get("Station_Name"))