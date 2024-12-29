lista = [] # número a ser acertado: 20
tentativas = 0

while True:
    
    usuario = input("Digite um valor: ")
    
    tentativas += 1
    
    print('-' * 20)
    
    try:
        usuario = int(usuario)
    except ValueError:
        print("Digite apenas valores inteiros")
        continue
    
    if usuario == 20:
        print("Você acertou o número!")
        break
    
    if usuario in lista:
        print(f'O Valor número: "{usuario}" já foi digitado anteriormente')
    else:
        print(f'O valor digitado: "{usuario}" está incorreto')
        lista.append(usuario)
    
print("Valores digitados anteriormente:", lista)
print("Total de tentativa(s):", tentativas)