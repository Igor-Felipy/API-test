import requests
#tipos de  requisição http:
r1 = requests.get("")#solicita
r2 = requests.post("")#cria
r3 = requests.put("")#atualiza/substitui
r4 = requests.delete("") #apaga
r5 = requests.head("")#solicita apenas o cabeçalho
r6 = requests.options("")#opções de comunicação