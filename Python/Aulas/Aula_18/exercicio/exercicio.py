while True:
    try:
        numero_1 = float(input("Digite o primeiro valor: ").replace(",", "."))
        numero_2 = float(input("Digite o segundo valor: ").replace(",", "."))
        break
    except ValueError:
        print("Por favor, digite apenas números: ")

if numero_1 > numero_2:
    print(f'O primeiro valor: {numero_1:.1f} é maior que o segundo valor: {numero_2:.1f}')        
elif numero_1 < numero_2:
    print(f'O segundo valor: {numero_2:.1f} é maior que o primeiro valor: {numero_1:.1f}')
else:
    print(f'Primeiro valor: {numero_1:.1f}, segundo valor: {numero_2:.1f}, são números iguais')