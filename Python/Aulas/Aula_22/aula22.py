# nome = 'Jonathan'

# print('a' in nome)
# print('a' not in nome) # não esqueça, o not in inverte os valores

nome = input("Digite o seu nome: ")
verificar = input("O que você deseja verificar? ")

if verificar in nome:
    print(f'{verificar} está entre {nome}')
else:
    print(f'{verificar} não está entre {nome}')