dados_pessoais = {
    'nome': 'Jonathan',
    'sobrenome': 'Marquezini',
    'idade': 20,
    'altura':1.75,
    'endereço': [
        {'rua': 'Rua josé nascimento'},
        {'número': 31},
        {'cidade': 'São Paulo'},
        {'estado': 'SP'},
        {'ponto de referência': 'Não tem'},
    ]
}

# pessoa = dict(nome= 'Jonathan', sobrenome= 'Marquezini')

print(dados_pessoais['nome'])
print(dados_pessoais['sobrenome'])
print()

for i in dados_pessoais:
    print(i, dados_pessoais[i])