import requests

nome = requests.get('http://gerador-nomes.herokuapp.com/nome/aleatorio').content
print(nome)