# for + range

# range -> (start, stop, step)

# teste 1

teste = 123

for i in range(3):

    user = input("Digite a sua senha: ")
    
    try:
        user = int(user)
    except ValueError:
        print("Digite apenas números")
        
    if user == teste:
        print("Você entrou no sistema")
        break
        
    if i < 2:
        print(f'Senha incorreta, você tem mais {2 - i} tentativa(s)')
        continue
    
print("Você excedeu o limite de tentativas. Sistema encerrado")

# teste 2

numeros = range(0, 10, 2)

user = int(input("Digite um número inteiro: "))

if user in range(0, 5):
    print("Esse valor está entre 0 a 5")
elif user in range(6, 8):
    print("Essa valor está entre 6 a 8")
elif user in range(9, 11): # não esqueça, na função range o pyhton não considera o número final
    print("Esse valor está entre 9 a 10")
else:
    print("Não reconheço esse valor")

# teste 3

usuario = int(input("Nos informe um númeo inteiro: "))

contador = range(usuario + 1)

for numero in contador:
    print(numero)