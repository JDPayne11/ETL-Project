import requests
import pandas as pd

url = f'https://eodhd.com/api/exchange-symbol-list/US?api_token=66ef5afcc7de75.85426574&fmt=json'
r = requests.get(url).json()
data = r.text
df = pd.read_json(data)
df