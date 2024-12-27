while True:
    print('Obs: caso você queria encerrar o sistema, digite: Sair')
    
    print("-" * 50)
        
    usuario = input("Qual tipo de conta você deseja fazer: (soma, subtração, divisão ou multiplicação): ").lower().strip()
    
    if usuario == 'sair':
        print("Você saiu do sistema. até breve")
        break
    
    if usuario not in ['soma', 'subtração', 'subtracao', 'divisão', 'divisao', 'multiplicação', 'multiplicacao']:
        print("Opção inválida, digite apenas o nome dos operadores")
        continue
        
    try:
        
        valor_1 = float(input("Digite o primeiro número: "))
        valor_2 = float(input("Digite o segundo número: "))
        
        if usuario == 'soma':
            print(f'a soma de {valor_1} + {valor_2} = {valor_1 + valor_2}')
            
        elif usuario == 'subtração' or usuario == 'subtracao':
            print(f'a subtração de {valor_1} - {valor_2} = {valor_1 - valor_2}')
            
        elif usuario == 'divisão' or usuario == 'divisao':
            print(f'a divisão de {valor_1} / {valor_2} = {valor_1 / valor_2}')
            
        elif usuario == 'multiplicação' or usuario == 'multiplicacao':
            print(f'a multiplicação de {valor_1} x {valor_2} = {valor_1 * valor_2}')
            
        else:
            print("Opção inválida, digite apenas operadores indicador")
            continue
            
    except ValueError:
        print("Valor inválido, digite apenas valores numéricos")