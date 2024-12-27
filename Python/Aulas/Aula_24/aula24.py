# 'preenchimento com espaços'

alfabeto = 'ABC'

print(f'{alfabeto: >10}') # ele auto preenche os espaços da esquerda para a direita até completar os espaços
print(f'{alfabeto: <10}') # ele auto preenche os espaços da direita para a esquerda até completar os espaços
print(f'{alfabeto: ^10}') # posiciona a string no centro

# modificando valores

valor = 1850

print(f'{valor:,.2f}') # valor modificando as casas decimais
print(f'{valor:-,.2f}') # 'valor negativo'
print(f'{valor:+,.2f}') # valor positivo

largura = 10

print(f'{valor: ^{largura},.2f}')