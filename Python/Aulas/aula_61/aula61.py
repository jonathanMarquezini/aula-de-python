# 54795725047

import re
# Recebe o CPF, remove os caracteres não numéricos e limpa os espaços
CPF = re.sub(r'[^0-9]', '', input("Me informe o seu cpf sem ponto/traço: ").strip())

cpf_nove_digitos = CPF[:9]
contador = 10

conta = 0

for numero in cpf_nove_digitos:
    conta += int(numero) * contador
    contador -= 1

primeiro_digito = (conta * 10) % 11 # primeiro digito = OK
digito_1 = primeiro_digito if primeiro_digito <= 9 else 0


cpf_dez_digitos = cpf_nove_digitos + str(digito_1)

contador_2 = 10
conta_2 = 0

for numero_2 in cpf_dez_digitos:
    conta_2 += int(numero_2) * contador
    contador_2 -= 1

segundo_digito = (conta_2 * 10) % 11 # segundo digito = OK
digito_2 = segundo_digito if segundo_digito <= 9 else 0

# print(f'Primeiro digito: {digito_1}')
# print(f'Segundo digito: {digito_2}')

cpf_gerado = f'{cpf_nove_digitos}{digito_1}{digito_2}'

cpf_formatado = f'{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}'

if CPF == cpf_gerado:
    print(f'CPF válido: {cpf_formatado}')

else:
    print('CPF inválido')