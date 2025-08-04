import json

# Load your GeoJSON (as a dict)
with open("output_points.geojson") as f:
    geojson_data = json.load(f)

# Convert to desired format
entry_gates = []

for feature in geojson_data["features"]:
    station = feature["properties"].get("Station")
    gate_name = feature["properties"].get("descriptio")
    lng, lat = feature["geometry"]["coordinates"]  # GeoJSON uses (lng, lat)

    entry_gates.append({
        "station": station,
        "gate_name": gate_name,
        "lat": lat,
        "lng": lng
    })

# Optional: Save to a new JSON file
with open("formatted_entry_gates.json", "w") as out_file:
    json.dump(entry_gates, out_file, indent=2)

# Print result
print(entry_gates)
