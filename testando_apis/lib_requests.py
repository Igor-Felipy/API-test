import requests
#tipos de  requisição http:
r1 = requests.get("")#solicita
r1.text
r1.json
r1.content
r1.status_code
r1.cookies['nome de um cookie']
r1.url
r1.history


r2 = requests.post("end point", data={'key':'value'})#cria

r3 = requests.put("")#atualiza/substitui
r4 = requests.delete("") #apaga
r5 = requests.head("")#solicita apenas o cabeçalho
r6 = requests.options("")#opções de comunicação