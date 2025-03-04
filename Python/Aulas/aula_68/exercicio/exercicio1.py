# Crie uma função que mutiplique todos os argumentos não nomeados
# Retorno o total para uma variavel e mostre o valor da variavel

def multiplicacao(*args):
    total = 1

    for i in args:
        total *= i
        
    return total

multiplicacao_1_2_3 = multiplicacao(1, 2, 3)
print(multiplicacao_1_2_3)