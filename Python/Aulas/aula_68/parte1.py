x, y, *resto = 1, 2, 3, 4, 5

print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    # args = list(args)
    # print(args, type(args))
    total = 0
    for numero in args:
        total += numero
        # print('Antes', numero)

        print(f'Depois, {total} + {numero} = {total}')
soma(1, 2, 3, 5, 6, 7)