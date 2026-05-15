#!/usr/bin/env python3
import requests

playload = {
	"device":"s-01",
	"temperature":37.9,
	"humidity":72,
	"location":"Bankok"
}

res = requests.post("https://httpbin.org/post",json=playload)
data = res.json()
print(f"""
Status: {res.status_code}
Data sent: {data["json"]}
Content-Type: {data["headers"]["Content-Type"]}
""")
