import requests
import pandas as pd

#response = requests.get("https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1")
#print(response.status_code)

#403 non ho la chiave per accedere
# mi serve l'headers con la chiave

url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data['records'])
print(df.head())