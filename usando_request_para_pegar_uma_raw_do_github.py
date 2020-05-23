import requests 

test = requests.get("https://raw.githubusercontent.com/alura-cursos/1576-mlops-machine-learning/aula-5/casas.csv")
print(test.text)