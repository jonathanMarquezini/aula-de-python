# parte 1

def soma(a, b):
    print(a + b)

soma(1, 2)  # argumentos posicionais (não nomeados)

# parte 2

def subtracao(x, y):
    print(x - y)

subtracao(x=3, y=2) # argumentos nomeados

# parte 3 (solicitando os valores pro usuário )

def user():
    
    while True:

        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Divisão')
        print('4 - Multiplicação')
        print('5 - Sair')

        usuario = input("Informe uma opção: 1-5 ")

        if usuario == '5':
            print("Você saiu do sistema")
            break

        i = float(input("Informe o primeiro valor: "))
        j = float(input("Informe o segundo valor: "))

        if usuario == '1':
            print(f'{i} + {j} = {i + j}')

        elif usuario == '2':
            print(f'{i} - {j} = {i - j}')
        
        elif usuario == '3':
            if j != 0:
                print(f'{i} / {j} = {i / j}')
            else:
                print("Erro: Divisão por zero não é permitida.")
        
        elif usuario == '4':
            print(f'{i} x {j} = {i * j}')
        
        else:
            print('Opção inválida')

user()