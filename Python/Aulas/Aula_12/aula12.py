nome = 'Jonathan Marquezini Fragali'
altura = 1.75
peso = 75.5
imc = peso / (altura * altura)

# f-strings
linha_1 = f'{nome}, tem: {altura:.2f} altura'
linha_2 = f'pesa: {peso}kgs e o seu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Formatando "string" em dinheiro 
dinheiro = 1650
vr = 638
print(f'seu salário é de {dinheiro:,.2f} + {vr:,.2f} de vale refeição')

# Formatando "string" no imc para casas decimais
# no local aonde fica a numeração "2", é ali aonde você vai indicar quantas casas decimais será impressa
print(f'{imc:.2f}') 