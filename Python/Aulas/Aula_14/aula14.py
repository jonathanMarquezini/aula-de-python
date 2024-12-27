# Usando input() para coletar os dados dos usuários

nome = input("Digte seu nome: ")

print(f'Seu nome é: {nome=}')

"""
{nome=}, um jeito de pegar o nome da variavel + o valor, é só você colocar o sinal de igual (=)
"""


# recebendo os dados e fazendo a soma dos números 

"""
Obs: essa foi feita de uma maneira iniciante, pois caso o usuário digite alguma letra ao invés de números,
o sistema quebraria logo na primeira linha (no caso na linha 15) e o desenvolverdor não saberia qual foi o
dado recebido
""" 
print("Fazendo a soma de dois números!")

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

print(f'a soma dos números é: {numero_1 + numero_2}')


"""
Obs: aqui já foi feita de uma maneira mais "experiente", pois caso o usuário digite algo além de númers, 
o sistema irá receber esses dados e apenas dará erro na hora da conversão (entre a linha 32 e 33) e o fim do sistema.

Nesse modelo, o desenvolvedor poderá verificar o erro e os dados recebidos referem ao erro no sistema.
"""

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

convert_numero1 = int(numero1)
convert_numero2 = int(numero2)

print(f'A soma dos dois valores é: {convert_numero1 + convert_numero2}')