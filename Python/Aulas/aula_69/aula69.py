# EX 1
def saudacao(msg):
    return msg

def teste_funcional(funcao, resto):
    return funcao(resto)

valor = teste_funcional(saudacao, 'Bom dia')
print(valor)


# EX 2
def multiplicacao(x, y):
    return x * y

def resultado(funcao, x, y):
    return funcao(x, y)

v12_turbo = resultado(multiplicacao, 2, 2)
print(v12_turbo)

# EX 3
def saudacao(ola, nome):
    return f'{ola}, {nome}'

def resultado(funcao, *args):
    return funcao(*args)

valor = resultado(saudacao, 'Olá', 'Jonathan')
print(valor)

# EX 4
def soma(x, y, z):
    return x + y + z

def resultado(geral, x, y, z):
    return geral(x, y, z)

valor = resultado(soma, 1, 2, 3)
print(valor)