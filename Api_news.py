import requests

url = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-03-18&sortBy=publishedAt&apiKey=83a7b6ff2cc54ef0a21d8b2cf1f06c93'

r = requests.get(url)

print(r.json())