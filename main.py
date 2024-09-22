import requests

url = f'https://eodhd.com/api/exchange-symbol-list/{EXCHANGE_CODE}?api_token=66ef5afcc7de75.85426574&fmt=json'
data = requests.get(url).json()

print(data)