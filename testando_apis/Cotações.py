import urllib.request
import json
url = "https://economia.awesomeapi.com.br/all/BTC-BRL"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
for d in data:
    print(data)