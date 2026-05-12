#!/usr/bin/env python3
import requests

res = requests.get("https://httpbin.org/get")

data = res.json()

output= f"""
Status: {res.status_code}
My IP: {data["origin"]}
URL: {data["url"]}
Headers: {data["headers"]}
"""
print(output)
