'''Usare l’API di WhiskyHunter per scaricare dati in formato JSON e analizzarli all’interno di un
Jupyter notebook
Ad esempio: quando è stata venduta la bottiglia più cara e a che prezzo? Quale marca?'''
import pandas as pd

data_path = "Giorgia-ai-bootcamp-2025\python\WhiskyHunterData.json"
with open(data_path,newline='') as fd:
    reader = pd.read_json(fd)
    df = pd.DataFrame(reader)
print(df.head())
#print(df.describe())
#print(df.info())



