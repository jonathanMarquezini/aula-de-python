# imutáveis: str, int, float e bool
# nesse caso, imutáveis seria oque? Você não pode mudar os valores dentro da variavel
# EX:
#teste = 'Jonathan'
#teste[0] = 'R'

# string = 'Jonathan'
# string_1 = f'{string[:3]}ABC{string[3:]}' 
# print(string_1)

nome = input('Digite seu nome: ')
print(f'Bem vindo {nome.capitalize()}') # capitalize tranforma a primeira letra em maiúscula


matricula = input('Digite sua matricula: ')
print(f'sua matricula: {matricula.zfill(6)}') # preenche com zeros(0) a esqueda