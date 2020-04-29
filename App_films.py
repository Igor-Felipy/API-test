import requests
r = requests.get('http://www.omdbapi.com/?apikey=[b0b71888]&')
print(r.json())