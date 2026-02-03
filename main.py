# Ajay Kumar
# Algorithm to unify two different telemetry data models
# Converts ISO timestamp into milliseconds 

import json
from datetime import datetime
# Convert ISO timestamp to milliseconds
def iso_to_millis(iso_string):
    dt = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


# Unify both data models
def unify_data(data):

    timestamp = data["timestamp"]

    # Convert ISO string if needed
    if isinstance(timestamp, str):
        timestamp = iso_to_millis(timestamp)

    unified = {
        "deviceId": data["deviceId"],
        "timestamp": timestamp,
        "temperature": data["temperature"]
    }

    return unified


# Load files
with open("data-1.json") as f:
    data1 = json.load(f)

with open("data-2.json") as f:
    data2 = json.load(f)


# Convert both
result1 = unify_data(data1)
result2 = unify_data(data2)


print("Unified Data 1:", result1)
print("Unified Data 2:", result2)