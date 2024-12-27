# usando o operador lógico or

# exercicio 1

idade = int(input("Digite a sua idade: "))

if idade < 18 or idade >= 60:
    print("passe no endereço xxxxxx para receber o seu benefício!")
else:
    print("pela a sua idade, você não está apto a receber o benefício")
    
# exercicio 2

semaforo1 = input("Digite a cor do primeiro semáforo (Verde, Amarelo ou Vermelho): ").strip().capitalize()
semaforo2 = input("Digite a cor do segundo semáforo (Verde, Amarelo ou Vermelho): ").strip().capitalize()

if semaforo1 == "Verde" or semaforo2 == "Verde":
    confirmacao = input("Confirme as cores dos semáforos novamente digitando 'Ok' ou 'ok': ").strip().lower()
    
    if confirmacao == "ok":
        print("Pode seguir viagem.")
    else:
        print("Confirmação inválida. Reavalie as condições novamente.")
else:
    print("Não poderá seguir viagem até pelo menos um sinal ficar na cor verde.")
    
# exercicio 3

verificacao = input("Digite a primeira palavra que venha à mente: ")

if verificacao.startswith("A") or verificacao.startswith("a"):
    print("A condição foi atendida.")
else:
    print("A condição não foi atendida.")
    
# ----------------------------------------------------------------------------------------

# teste "solo"

while True:
    try:
        sistema = input("Você deseja [E]ntrar ou [S]air do sistema: ").lower()
        
        if sistema == "e":
            senhas = [1234, 12345]
            
            for x in range(3): # o usuário terá 3 tentativas
                senha_usuario = int(input("Digite a sua senha: "))
                
                if senha_usuario in senhas: # o IN verifica se o valor digitado pelo usuário está na lista indicada
                    print("Você entrou no sistema")
                    break
                else: 
                    print(f"Senha incorreta, você tem mais {2 - x} tentativas: ")
            else:
                print("Você errou as 3 tentativas, fim do sistema...")
                break
                
        elif sistema == 's':
            print("Você saiu do sistema, até mais...")
        else:
            print("Opção incorreta, use (E) para entrar no sistema ou (S) para sair do sistema")
    except ValueError:
        ...