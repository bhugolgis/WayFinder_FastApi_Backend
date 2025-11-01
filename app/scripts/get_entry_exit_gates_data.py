import json

# Load your GeoJSON (from the pasted text)
geojson_data = json.loads(open("D:\Pranav\Projects\wayfinder\src\components\Map\Entry_Exits_Polygon.geojson").read())

# Station name mapping
station_name_map = {
    "Cuffe Parade": "Cuffe Parade",
    "Vidhan Bhavan Metro Statiob": "Vidhan Bhavan",
    "Churchgate Metro Station": "Churchgate Metro",
    "Hutatma Chowk": "Hutatma Chowk",
    "CSMT Metro": "Chhatrapati Shivaji Maharaj Terminus Metro",
    "Kalbadevi Metro Station": "Kalbadevi",
    "Girgaon Metro Station": "Girgaon",
    "Grant Road Metro": "Grant Road Metro",
    "Jaganath Shankar Seth Metro": "Jagannath Shankar Sheth Metro",
    "Mahalakshmi": "Mahalaxmi Metro",
    "Science Centre": "Science Centre",
    "Acharya Atre Chowk": "Acharya Atre Chowk",
    "Worli": "Worli",
    "Siddhivinayak": "Siddhivinayak",
    "Dadar": "Dadar Metro",
    "Shitala Devi Mandir": "Shitala Devi Mandir",
    "Dharavi": "Dharavi",
    "Bandra Kurla Complex": "Bandra-Kurla Complex",
    "Bandra colony": "Bandra Colony",
    "Santacruz": "Santacruz Metro",
    "CIA T1": "Chhatrapati Shivaji Maharaj International Airport-T1",
    "Sahar Road": "Sahar Road",
    "CSMIA T2": "Chhatrapati Shivaji Maharaj International Airport-T2",
    "CSMI T2": "Chhatrapati Shivaji Maharaj International Airport-T2",
    "Marol Naka": "Marol Naka",
    "MIDC Andheri": "MIDC-Andheri",
    "seepz": "SEEPZ",
    "Seepz": "SEEPZ",
    "SEEPZ": "SEEPZ",
    "Aarey JVLR": "Aarey JVLR"
}

def compute_centroid(multi_polygon_coords):
    # Take first polygon, first linear ring
    ring = multi_polygon_coords[0][0]
    lats = [pt[1] for pt in ring]
    lngs = [pt[0] for pt in ring]
    return sum(lats) / len(lats), sum(lngs) / len(lngs)

entry_gates = []

for feature in geojson_data["features"]:
    props = feature["properties"]
    geom = feature["geometry"]
    
    raw_station = props["Station"]
    gate_name = props["descriptio"]
    
    if raw_station not in station_name_map:
        print(f"⚠️ Unmapped station: {raw_station}")
        continue
        
    canonical_station = station_name_map[raw_station]
    lat, lng = compute_centroid(geom["coordinates"])
    
    entry_gates.append({
        "station": canonical_station,
        "gate_name": gate_name,
        "lat": lat,
        "lng": lng
    })

# Optional: Save or print
import pprint
pprint.pprint(entry_gates)