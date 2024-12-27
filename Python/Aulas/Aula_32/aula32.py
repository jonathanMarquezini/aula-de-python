print("Bem-vindo ao nosso contador negativo")

while True:
    usuario = input("Nos informe um número alto: ")
    
    if usuario.isdigit():
        usuario = int(usuario)
        
        contador = usuario
        
        while contador >= 0:
            print(contador)
            contador -= 1
            
        print("Contagem concluída")
        break
    
    else:
        print("Digite apenas valores inteiros")