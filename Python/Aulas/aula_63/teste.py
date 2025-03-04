import random
import sys

for _ in range(9):

    cpf_nove_digitos = ''

    for i in range(9):
        cpf_nove_digitos += str(random.randint(0,9))

    contador = 10
    divisao_valores = 0

    for digito in cpf_nove_digitos:
        divisao_valores += int(digito) * contador
        contador -= 1

    primeiro_digito = (divisao_valores * 10) % 11 # primeiro digito gerado

    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

    CPF_2 = cpf_nove_digitos + str(primeiro_digito)

    contador_2 = 11
    divisao_valores_2 = 0

    for numero_2 in CPF_2:
        divisao_valores_2 += int(numero_2) * contador_2
        contador_2 -= 1

    segundo_digito = (divisao_valores_2 * 10) % 11

    segundo_digito = segundo_digito if segundo_digito <= 9 else 0

    # print(f'primeiro digito: {primeiro_digito}')
    # print(f'segundo digito: {segundo_digito}')

    cpf_gerado = f'{cpf_nove_digitos}{primeiro_digito}{segundo_digito}'

    cpf_formatado = f'{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}'

    print(cpf_formatado)