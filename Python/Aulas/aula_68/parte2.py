x, y, *resto = 1, 2, 3, 4, 5

print(x, y, resto)

def soma(*args):

    total = 0

    for i in args:
        total += i

    return total

# soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

# print(sum((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 78, 10
soma_1_2_3 = soma(*numeros)

print(sum(numeros))