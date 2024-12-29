nomes = ['Jonathan', 'Marquezini', 'Fragali']

usuario = input("Digite um nome/sobrenome: ")

if usuario in nomes:
    print('Você acertou!')
else:
    print(f'esse nome/sobrenome "{usuario}" não tem na lista')
    
for i in nomes:
    print(i)