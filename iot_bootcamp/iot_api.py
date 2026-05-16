#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
	value: float
	battery: float

@app.get("/")
def root():
	return{
		"message": "IoT API Server",
		"version": "1.0",
		"Status": "running"
	}

@app.get("/device/{device_id}")
def list_sensor(device_id: str):
	return{
		"device_id": {device_id},
		"type": "Temperature",
		"unit": "celsius"
	}


@app.post("/device/{device_id}/report")
def receive_data(device_id: str,data: SensorData):
	status = bool(data.value and data.battery)
	return{
		"device_id": device_id,
		"value": data.value,
		"battery": data.battery,
		"recorded": status
	}
