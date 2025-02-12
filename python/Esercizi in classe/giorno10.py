import requests
import pandas as pd
response = requests.get(
"https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1",
headers={"x-api-key": "DEMO_KEY"}
)
print(response.status_code)