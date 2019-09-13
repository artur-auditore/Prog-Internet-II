import requests

print('Informa o valor do bitcoin (Atualizado em 13/09/2019)') 

#json_original = https://api.coindesk.com/v1/bpi/currentprice.json
#json_modificada = http://www.json-generator.com/api/json/get/bTwonkmGeW?indent=2

url = 'http://www.json-generator.com/api/json/get/bUrNHrYVua?indent=2'

response = requests.get(url)
json = response.json()

valor = json ['bpi']['BR']['rate']

print('O valor atual do bitcoin é: R$' + valor)

#json criado em: http://www.json-generator.com.
