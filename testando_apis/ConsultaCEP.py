import requests


def main():
    print('########################')
    print('######Consulta CEP######')
    print('########################')
    print()

    # Entrada do cep e validação do mesmo
    cep_input = input('Digite o CEP para consulta: ')
    print('\n\n\n')
    if len(cep_input) != 8:
        print('Quantidade de digitos inválida!')
        exit()

    # Requisiçao para a API, verificaçao de erro e apresentação de resultado.
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    address_data = request.json()
    if 'erro' not in address_data:
        print('==> CEP ENCONTRADO <==\n')
        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('complemento: {}'.format(address_data['complemento']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))
    else:
        print('{}: CEP inválido!'.format(cep_input))

    option = int(input('\n\nDeseja realizar uma nova consulta? \n1. SIM\n2. SAIR\n'))
    if option == 1:
        main()
    else:
        print('Saindo...')

if __name__ == '__main__':
    main()
