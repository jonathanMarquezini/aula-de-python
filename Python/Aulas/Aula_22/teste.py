nomes = []  # Lista vazia

print("Adicione os nomes para outros usuários tentarem adivinhar")

while True:
    try:
        adicionar = input("Digite um nome ou digite (fim) para encerrar a adição de nomes: ").strip().lower()
        
        if adicionar == 'fim': 
            break
        
        if adicionar.isalpha():  # Verifica se a entrada contém apenas letras
            nomes.append(adicionar)  # Adiciona o nome à lista
        else:
            print("Entrada inválida, digite apenas letras.")
        
    except ValueError as a:
        print(a)

if nomes:
    print("\nNomes adicionados ao jogo:")
    for adicionar in nomes:
        print(f"- {adicionar.capitalize()}")
else:
    print("\nNenhum nome foi adicionado ao jogo.")

    

print("Bem Vindo ao jogo de adivinhação, o jogo é bem simples, você precisa apenas acertar o nome de uma pessoa que foi adicionado por outro usuário")

while True:
    try:
        usuario = input("Primeira tentativa: ").lower()
        
        if not usuario.isalpha():
            raise ValueError("Entrada inválida, digite apenas letras.")
        
        if usuario in nomes:
            print("Você acertou, fim de jogo...")
            break
        
        for i in range(3):
            tentativas = input(f"Você errou, você tem apenas mais {3 - i} tentativa(s): ").lower()
            
            if not tentativas.isalpha():
                raise ValueError("Entrada inválida, digite apenas letras.")
            
            if tentativas in nomes:
                print("Parabéns, você acertou, fim de jogo...")
                exit() # encerra o programa
        
        print("Acabaram as suas tentativas, GAME OVER.")
        break
                
    except ValueError as e:
        print(e)  # Exibe uma mensagem de erro personalizada