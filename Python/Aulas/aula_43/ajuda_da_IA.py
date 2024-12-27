palavra = 'python'
tentativas = 0
max_tentativas = 5
palavra_oculta = ['_'] * len(palavra)  # Esconde a palavra com '_'

print("Bem-vindo ao Jogo da Forca!")
print("Você tem 5 tentativas para acertar a palavra.")

while tentativas < max_tentativas:
    print(f"\nPalavra: {' '.join(palavra_oculta)}")
    
    usuario = input("Digite uma letra: ").lower()
    
    if len(usuario) > 1:
        print("Digite apenas uma letra")
        continue
    
    if usuario in palavra:
        print(f'Você acertou! A letra {usuario} tem no jogo')
        
        for i in range(len(palavra)):
            if palavra[i] == usuario:
                palavra_oculta[i] = usuario
    
    else:
        tentativas += 1
        print(f'Você errou!, A letra {usuario} não tem no jogo')
        print(f'Você tem mais {max_tentativas - tentativas} tentiva(s)')
    
    if '_' not in palavra_oculta:
        print(f"\nParabéns! Você acertou a palavra era: {''.join(palavra_oculta)}")
        break
    
if tentativas == max_tentativas:
    print(f"\nVocê perdeu! A palavra era: {palavra}")