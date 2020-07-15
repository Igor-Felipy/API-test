import requests

a = requests.get('https://api.adviceslip.com/advice').json()['slip']['advice']

print(a)

with open("conselhos.txt", "a") as conselhos:
    conselhos.write('\n' + a )