frase = (
    'O python é uma linguagem de programação multiparadigma. '
    'O python foi criado por Guido van Rossum.'
)

indice = 0 

letras_repete = 0
qtd_repete = ''

while indice < len(frase):
    letra = frase[indice]
    
    if letra == ' ':
        indice += 1
        continue
    
    repeticao_atual = frase.count(letra)
    
    while letras_repete < repeticao_atual:
        letras_repete = repeticao_atual
        qtd_repete = letra
    
    
    indice += 1
    
print(f"A letra que mais vezes apareceu foi: '{qtd_repete}' = {letras_repete}x")