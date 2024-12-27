sistema = input("Você deseja [E]ntrar ou [S]air do sistema: ").lower()

if sistema == "e":
    
    senhas = [12345, 123456]
    senha_usuario = int(input("Digite a sua senha: "))
    
    if senha_usuario in senhas:   # o IN verifica se a senha está na lista de senhas
        input("Você entrou no sistema")
    else:
        input("Senha inválida, fim do sistema")
elif sistema == "s":
    print("Você saiu do sistema, até mais...")
else:
    print("Opção inválida, tente novamente")