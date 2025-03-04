# Crie uma função, fala se é número impar ou par
# retorne se for par ou ímpar

def impar_par():
    usuario = input("Informe um valor: ")

    if not usuario:
        print('Campo vazio')
        return
    
    usuario = int(usuario)

    if  usuario % 2 == 0:
        print('Par')
    else:
        print('Impar')

    return usuario

impar_par()