try:
    NP1 = float(input('Digite sua nota da np1: '))
    NP2 = float(input('Digite sua nota da np2: '))
    PIM = float(input('Digite sua nota do pim: '))
    RESULTADO = (NP1 * 0.4) + (NP2 * 0.4) + (PIM * 0.2)
    
    if NP1 and NP2 and PIM:
        if RESULTADO >= 7:
            print(f'Você foi aprovado, nota final: {RESULTADO:.2f}')
        elif RESULTADO <= 6:
            print('Você ficou de exame')
            EXAME = float(input('Digite sua nota do exame: '))
        
            NOTA_FINAL = (RESULTADO + EXAME) / 2         
            if NOTA_FINAL >= 5:
                print(f'Você foi aprovado sua nota final é: {NOTA_FINAL:.2f}')
            else:
                print(f'Você foi reprovado, nota final: {NOTA_FINAL:.2f}')
except ValueError:
    print('Você deixou algum campo vazio, fim do sistema')