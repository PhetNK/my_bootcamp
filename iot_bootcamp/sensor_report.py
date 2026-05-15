#!/usr/bin/env python3
import requests

url = "https://httpbin.org/"

headers={
"X-Api-Key":"iot-secret-001"
}

res = requests.get(url+"get",headers=headers)
get_data = res.json()

playload = {
"device":"sensor-01",
"temp": 37.9,
"hum": 79
}

update = requests.post(url+"post",json=playload)
post_data = update.json()

report = f"""
Server: {get_data["origin"]}
Device: {post_data["json"]["device"]}
Temperature: {post_data["json"]["temp"]}
Humidity: {post_data["json"]["hum"]}
API Key used: {get_data["headers"]["X-Api-Key"]}
Status: {update.status_code}
"""

print(report)
