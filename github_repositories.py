import base64
from github import Github

username = input("entre com o seu nome de usuario do github: ")

g = Github()

user = g.get_user(username)

for repo in user.get_repos():
    print(repo.full_name)