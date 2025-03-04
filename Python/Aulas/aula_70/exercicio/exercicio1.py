# # Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro

# def calculo(numero):
#     def resultado(operador):
#         return numero * operador
#     return resultado

# duplicar = calculo(2)
# triplicar = calculo(3)
# quadriplicar = calculo(4)

# print(duplicar(2))
# print(triplicar(2))
# print(quadriplicar(2))

def soma(numero):

    def resultado(caracter):
        return numero * caracter
    
    return resultado

v1 = soma(2)
v2 = soma(3)
v3 = soma(4)

print(v1(2))
print(v2(3))
print(v3(4))