nome = "Jonathan"
altura = 1.75
peso = 76
imc = peso / (altura * altura)

# concatenação menos utilizada

print(nome + " tem " + str(altura) + " de altura, e seu peso atualmente está em: " + str(peso) + "Kg,\nseu IMC atualmente está em: " + str(imc))

# utlizando f'strings (concatenação mais utlizada)

print(f'{nome} tem {altura} de altura, seu peso atualmente está em: {peso}Kg, e o seu imc atualmente está em: {imc:.2f}')