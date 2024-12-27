nome = input("Digite o seu primeiro nome: ")
salario = float(input("Informe o seu salário: "))

salario_minimo = 1412

if salario > salario_minimo * 2:
    print("%s, seu salário é de R$%.2f, então você recebe mais de um salário minimo" % (nome, salario))
elif salario >= salario_minimo and salario < salario_minimo * 2:
    print("%s, seu salário é de R$%.2f, então você recebe um salário minimo" % (nome, salario))
else:
    print("%s, seu salário é de R$%.2f, então você receber menos que um salário miniomo" % (nome, salario))
    
# usando interpolação com hexadecimal

print('-' * 10)

print("o hexadecimal de %d é %x" % (15, 15))
print("o Hexadecimal de %d é %08X" % (92, 92))