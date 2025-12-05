import requests

saida = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
print(saida.json()['USDBRL']['bid'])