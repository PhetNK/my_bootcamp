#!/usr/bin/env python3
import requests

params = {"Device":"sensor-01","location":"Bangkok"}
headers = {
"User-Agent":"IoTBot/1.0",
"X-Api-Key":"test001"
}

res = requests.get("https://httpbin.org/get",params=params,headers=headers)

data = res.json()

output= f"""
Status: {res.status_code}
My IP: {data["origin"]}
URL: {data["url"]}
Headers: {data["headers"]}
"""

print(f"""
URL: {data["url"]}
Headers seen by server: {data["headers"]}
""")
