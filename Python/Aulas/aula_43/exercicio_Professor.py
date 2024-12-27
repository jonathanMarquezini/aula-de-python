import os

palavra_secreta = 'python'
palavra_descoberta = ''
tentativas = 0

print("Bem vindo ao nosso jogo da forca, tente a certa a palavra com menos tentativas. BOA SORTE!")
print("-" * 25)

while True:
    usuario = input("Digite uma letra: ").lower()
    tentativas += 1
    
    if len(usuario) > 1:
        print("Digite apenas uma letra")
        continue
    
    if usuario in palavra_secreta:
        palavra_descoberta += usuario
        
    palavra_formada = ''
    
    for descoberta in palavra_secreta:
        if descoberta in palavra_descoberta:
            palavra_formada += descoberta
        else:
            palavra_formada += '_'
            
    print("Palavra formada:", palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('-' * 25)
        print("Você ganhou, parabéns!")
        print(f'A palavra era: {palavra_formada}')
        print(f'Número de tentativas: {tentativas}')
        
        if tentativas == 6:
            print("Parabéns, você não errou nenhuma palavra!")
        else:
            break