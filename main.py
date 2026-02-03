# Ajay Kumar
# Algorithm to unify two different telemetry data models
# Converts ISO timestamp into milliseconds 

import json
from datetime import datetime


def iso_to_millis(iso_string):
    dt = datetime.fromisoformat(iso_string.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


def unify_data(data):
    timestamp = data["timestamp"]

    if isinstance(timestamp, str):
        timestamp = iso_to_millis(timestamp)

    return {
        "deviceId": data["deviceId"],
        "timestamp": timestamp,
        "temperature": data["temperature"]
    }


with open("data-1.json") as f:
    data1 = json.load(f)

with open("data-2.json") as f:
    data2 = json.load(f)


result1 = unify_data(data1)
result2 = unify_data(data2)


print(json.dumps(result1))
print(json.dumps(result2))