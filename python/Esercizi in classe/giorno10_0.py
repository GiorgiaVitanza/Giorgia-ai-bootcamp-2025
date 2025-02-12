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
#print(df.head())

import requests
from bs4 import BeautifulSoup
url = "https://www.google.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.body.text)
start_url = "https://www.google.com"
for a in soup.find_all("a"):
    a_href = a.attrs['href']
    if a_href.startswith('http'):
        url = a_href
    else:
        url = start_url + a_href
    response_top = requests.get(url)




ignored = [ "index.html"]
base_url = "https://books.toscrape.com/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text,features="html.parser")
links = soup.find_all('a')
#print(links)
for link in links:
    link_rel = link.attrs['href']
    if link_rel in ignored:
        continue
    url = base_url + link_rel
    print(url)
link = links[1]
print(link)

