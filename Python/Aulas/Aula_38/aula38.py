usuario = input("Digite algum texto/frase/palavra: ").strip()

if not usuario:
    print("Campo vazio, você precisa digitar alguma coisa: (texto/frase/palavra)")
    
else:
        
    indice = 0 
    contagem = 0
    string_vazia = ''

    while indice < len(usuario):
        letra = usuario[indice]
    
        if letra == ' ':
            indice += 1
            continue
    
        repeticao = usuario.count(letra)
    
        if contagem < repeticao:
            contagem = repeticao
            string_vazia = letra
    
        indice += 1
    
    print(f'a letra que mais se repete: "{string_vazia}" = {contagem}x')