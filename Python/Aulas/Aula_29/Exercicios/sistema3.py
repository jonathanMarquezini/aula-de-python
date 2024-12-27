while True:
    try: 
        usuario = input("Informe-nos o seu primeiro nome: ")
        
        if not usuario.isalpha(): # Permite espaços, mas verifica apenas letras
            print("Contém caracteres inválidos")
            continue
        
        if len(usuario) <= 4:
            print("Seu nome é curto")
        elif len(usuario) >= 5 and len(usuario) <= 6:
            print("seu nome é medio")
        else:
            print("Seu nome é grande")
            
    except ValueError:
        print("Use apenas caracteres do tipo texto")