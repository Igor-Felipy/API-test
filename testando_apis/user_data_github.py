import requests

username = "Igor-Felipy"

url = "https://api.github.com/users/" + username
user_data = requests.get(url).json()
print(user_data)