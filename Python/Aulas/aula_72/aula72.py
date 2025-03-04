pessoa = {
    'nome': 'Jonathan',
    'sobrenome': 'Marquezini',
    'idade': 20,
    'altura': 1.75,
    'endereço': [
        {'Rua': 'Rua são josé do nascimento'},
        {'Cidade': 'São Paulo'},
        {'Estado': 'São Pauloa'},
        {'UF': 'SP'},
        {'Bairro': 'xxxxx'},
    ],
} 

# criando uma nova chave
pessoa['peso'] = '75'

del pessoa['peso']

if pessoa.get('peso', 'chave não existe'):
    print('Chave encontrada')