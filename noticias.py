import requests
from bs4 import BeautifulSoup

url = 'http://www.fametro.edu.br/portal/index.php?u=noticias&c=197&cam='
req = requests.get(url)

#print(req.content)

soup = BeautifulSoup(req.content, 'html.parser')

lista_noticias = soup.find_all('ul', class_='media-list noticias')

#print(lista_noticias)

for lista_titulos in lista_noticias:
    lista = lista_titulos.find_all('h4', class_='media-heading')
    #print(lista)
    for lista_dados in lista:
        print(lista_dados.next_element)