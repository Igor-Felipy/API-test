import requests

url = 'http://newsapi.org/v2/everything?q=bitcoin&from=2020-03-18&sortBy=publishedAt&apiKey=23b824f208b94321b5980485a7738c6e'

r = requests.get(url)

print(r)