while True:
    try: 
        usuario = input("Nos informe qual o horário atual: ")
        
        if usuario.isdigit():
            
            horario_usuario = int(usuario)
            
            if horario_usuario >= 0 and horario_usuario <= 11:
                print("com base no seu horário atual, está na parte da manhã")
            elif horario_usuario > 11 and horario_usuario <= 18:
                print("com base no seu horário atual, está na parte da tarde")
            elif horario_usuario >= 19 and horario_usuario <= 23:
                print("com base no seu horário atual, está na parte da noite")
            else:
                print("Não reconheço esse horário")
        else:
            print("Digite apenas números inteiros")
    except ValueError:
        print("Digite apenas valores")