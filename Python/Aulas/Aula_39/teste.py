# for / in 

senha = 123

for tentativas in range(5):
    
    usuario = input("Digite a sua senha: ")
    
    try:
        usuario = int(usuario)
    except ValueError:
        print("Valor inválido, digite apenas números")
        continue
    
    if usuario == senha:
        print("Você entrou no sistema")
        break
    
    elif tentativas < 4:
        print(f'senha incorreta, você tem mais {4 - tentativas} tentativa(s)')

else:
    print("Você excedeu o limite de tentativas, programa encerrado...")