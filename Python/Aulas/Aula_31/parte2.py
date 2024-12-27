print("Bem-vindo ao sistema de contador")

while True:
    usuario = input("Digite o número que você quer que eu conte: ")
    
    if usuario.isdigit():
        usuario = int(usuario)
        
        contador = 0
        
        while contador <= usuario:
            print(contador)
            contador += 1
        
        print("Contagem concluída")
        break
    
    else:
        print("Informe apenas valores inteiros")    