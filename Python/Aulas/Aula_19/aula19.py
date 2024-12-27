# Usando and e or para a criação de um "sistema" em python

entrada = input("deseja [E]ntrar ou [S]air do sistema: ")

if entrada == "E" or entrada == "e":
    
    senha = 12345
    senha_usuario = int(input("Digite a sua senha: "))
    
    if senha_usuario == senha:
        print("Você entrou na sua conta")
    else: 
        print("Senha incorreta, fim do sistema")
        
elif entrada == "S" or entrada == "s":
    print("Você saiu do sistema, até mais...")
else:
    print("Opção inválido, sistema encerrado...")    