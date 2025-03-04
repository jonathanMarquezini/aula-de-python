def saudacao(msg):
    def saudar(nome):
        return f'{msg}, {nome}'
    
    return saudar

v1 = saudacao('Bom dia')
v2 = saudacao('Boa tarde')
v3 = saudacao('Boa noite')

print(v1('Jonathan'))
print(v2('Jonathan'))
print(v3('Jonathan'))