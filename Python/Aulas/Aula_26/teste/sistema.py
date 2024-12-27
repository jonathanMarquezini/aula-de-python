# sistema = input('[E]ntrar ou [S]air: ')
# senha_sistema = '12345'
# tentativas = 0
# max_tentativas = 3


# if sistema == 'E' or sistema == 'e':
#     senha_usuario = input('Digite sua senha: ')
    
#     while senha_usuario != senha_sistema:
#         tentativas += 1
        
#         if tentativas >= max_tentativas:
#             print('Você excedeu o número máximo de tentativas. Sistema bloqueado')
#             break # "encerra a linha"
        
#         senha_usuario = input('Senha incorreta, tente novamente: ')
    
#     if senha_usuario == senha_sistema: 
#         print('Você entrou no sistema')
        
# elif sistema == 'S' or sistema == 's':
#     print('Você saiu do sistema')
# else:
#     print('Opção incorreta, tenta (e) para Entrada ou (s) para saída')
    
# Evite duplicidade de código, isso deixará o código mais limpo e de fácil entendimento

senha_sistema = 12345
tentativas = 0
max_tentativas = 3

while True:
    try:
        usuario = input("[E]ntrar ou [S]air: ").lower()
        
        if usuario == 'e':
            while tentativas < max_tentativas:
                sistema = int(input("Digite a sua senha: "))
                
                if sistema == senha_sistema:
                    print("Você entrou no sistema")
                    break
                else:
                    tentativas += 1
                    
                    if tentativas < max_tentativas:
                        print(f"Tente novamente, restam {max_tentativas - tentativas} tentativas(s): ")
                    else:
                        print("Você excedeu o limite de tentativas, sistema bloqueado")
                        break
        elif usuario == 's':
            print("Você saiu do sistema")
        else:
            print("Opção inválida. Fim do sistema")
    except ValueError:
        print("Entrada inválida, tente novamente")