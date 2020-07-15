import requests
while True:
    filme = input('Digite o nome de um filme: ')
    r = requests.get(f'http://www.omdbapi.com/?apikey=dac9a156&t={filme}')
    dados = r.json()
    print(dados)
    print('Ano: {}'.format(dados['Year']))
    print('Tempo de filme: {}'.format(dados['Runtime']))
    print('Nota no MetaCritic: {}'.format(dados['Metascore']))
    input('Pressione <enter> para continuar!')