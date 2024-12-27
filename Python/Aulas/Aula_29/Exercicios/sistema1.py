while True:
    try: 
        usuario = input("Digite um valor inteiro: ")
        
        if usuario.isdigit():
            valor_usario = int(usuario)
            
            if valor_usario % 2 == 0:
                print("par")
            else:
                print("ímpar")
        else:
            print("Digite apenas valores inteiros")
    except ValueError:
        print("Digite apenas números")