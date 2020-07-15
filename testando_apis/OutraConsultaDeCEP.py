import requests


CEP= input('Digite o seu CEP: ')
if len(CEP) != 8:
    print('Quantidade de digitos invalida! ')
    exit()

request = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(CEP))
address_data = request.json()
print('==> CEP ENCONTRADO <==')
print('CEP: {}'.format(address_data['cep']))
print('{}: {}'.format(address_data['address_type'], address_data['address_name']))
print('Bairro: {}'.format(address_data['district']))
print('Cidade: {}'.format(address_data['city']))
print('Estado: {}'.format(address_data['state']))
