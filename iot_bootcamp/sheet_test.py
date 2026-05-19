#!/usr/bin/python3
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file("iot-bot_credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open("IoT-Sensor-Log").sheet1

sensors = [
    {"id": "temp-01", "temp": 37.5, "humidity": 80},
    {"id": "temp-02", "temp": 39.1, "humidity": 65},
    {"id": "humid-01", "temp": 36.8, "humidity": 90}
]

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
update_status={"complated":0,"fail":0,"alert": 0}
alert_sensor=[]
for sensor in sensors:
    status = "OK" if sensor["temp"] <= 38.5 else "HIGH"
    if status == "HIGH":
        alert_sensor.append(f"{sensor["id"]}({sensor["temp"]})")
        update_status["alert"] +=1

    data = [timestamp] + list(sensor.values()) + [status]
    try:
        sheet.append_row(data)
        update_status["complated"] +=1
    except:
        update_status["fail"] +=1
        pass


report=f"""
=== Sensor Log Complete ===
Logged {update_status["complated"]} records at {timestamp }
High temp alerts: {update_status["alert"]} {",".join(alert_sensor)}
Sheet URL: {sheet.url}
"""
print(report)