# iteráveis -> str, range, etc
# iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entregue o seu iterador

# nome = 'Python'.__iter__

# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())
# print(nome.__next__())

# nome = iter('Python')

# print(next(nome))
# print(next(nome))
# print(next(nome))
# print(next(nome))
# print(next(nome))
# print(next(nome))

nome = 'Jonathan' # iterável
iterador = iter(nome) # iterador = iter()

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break