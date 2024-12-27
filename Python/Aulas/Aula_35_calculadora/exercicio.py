while True:
    usuario = input('Deseja [E]ntrar ou [S]air do sistema: ').strip().lower() # strip().lower() = Remove espaços em branco extras e normaliza as entradas em minúsculas.
    
    if usuario.startswith('s'): # começa com
        print('Você saiu do sistema')
        break # encerra a linha
    
    elif usuario.startswith('e'):
        usuario = input('Qual calculo deseja fazer (Soma, Subtração, Divisão, Multiplicação): ').strip().lower()
        
        try:
            primeiro_valor = float(input('Digite o primeiro valor: '))
            segundo_valor = float(input('Digite o segundo valor: '))
            
            if usuario == 'soma':
                print(f'A soma de {primeiro_valor} + {segundo_valor} = {primeiro_valor + segundo_valor}')
                
            elif usuario == 'Subtração' or usuario == 'subtração':
                print(f'A subtração de {primeiro_valor} - {segundo_valor} = {primeiro_valor - segundo_valor}')
                
            elif usuario.startswith('d'): # d = Divisão
                if segundo_valor != 0:
                    print(f'A divisão de {primeiro_valor} / {segundo_valor} = {primeiro_valor / segundo_valor}')
                else:
                    print('Erro: divisão por zero')
                    
            elif usuario.startswith('m'): # m = Multiplicação
                print(f'A multiplicação de {primeiro_valor} x {segundo_valor} = {primeiro_valor * segundo_valor}')
                
            else:
                print('Operação inválida, Tente novamente')
                
        except ValueError:
            print('Erro: Digite apenas números válidos.')