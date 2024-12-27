import os

palavra_secreta = 'python'
palavra_certa = ''
tentativas = 0
max_tentativas = 10

usuario = input("[E]ntrar ou [S]air: ").lower()

while True:
    
    if usuario == 'e':
        
        if tentativas >= 10:
            print("Game over. Você atingiu o limite máximo de tentativas.")
            break
        
        player = input("Digite uma letra: ")
        tentativas += 1
        
        if len(player) > 1:
            print("Digite apenas uma letra")
            continue
        
        if player in palavra_secreta:
            palavra_certa += player
            
        string_vazia = ''
            
        for descoberta in palavra_secreta:
             
            if descoberta in palavra_certa:
                string_vazia += descoberta
            else:
                string_vazia += '_'
            
        print("Palavra descoberta:", string_vazia)
        print(f'tentativas restantes: {max_tentativas - tentativas}')
        
        if string_vazia == palavra_secreta:
            os.system('cls')
            print('Número de tentativas:', tentativas)
            print('Palavra formada', palavra_secreta)
            
            if len(palavra_certa) == 6:
                print("Caramba, você não errou nenhuma vez. PARABÉNS!")
                break
            
    elif usuario == 's':
       print("Você saiu do sistema, até mais...")
    else:
        print("Valor inválido, Tente novamente")
        break