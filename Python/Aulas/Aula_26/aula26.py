try:
    valor_1 = float(input("Digite o primeiro valor: "))
    valor_2 = float(input("Digite o segundo valor: "))
    
    print(f"a soma dos valores é: {valor_1 + valor_2}")
except ValueError:
    print('Tente novamente, isso não é um valor')