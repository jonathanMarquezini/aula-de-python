nome = 'hello world'

# [i:f:p] [::]

#  i = inicio

print(nome[0:]) # pega a string desde o inicio
print(nome[6:])

# fatiamento

print(nome[0:7]) # Obs: o indice final não é incluído, lembre de pegar um a mais do que o solicitado
print(nome[3:9])

# len -> soma dos caracteres dentro de uma string

# Obs: contagem de indices começa no zero (0) e também tem a contagem normal que inicia-se no um (1)

print(len(nome)) 

# Partes

print(nome[0:11:1])