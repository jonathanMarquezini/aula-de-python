frase = '    Olha só que    , coisa interessante       '
lista_palavras = frase.split(',') # estou dizendo: 'quebra na vírgula'

lista_organizada = []

for i, frase in enumerate(lista_palavras):
    lista_organizada.append(lista_palavras[i].strip())

# print(lista_palavras)
# print(lista_organizada)

# frase_unidas = ''.join(frase).strip()
frase_unidas = ','.join(lista_organizada)
print(frase_unidas)