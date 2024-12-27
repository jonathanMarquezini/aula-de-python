usuario = input("Digite o seu primeiro nome: ")

contador = 0

while contador < len(usuario):
    print(usuario[contador], end="*")
    contador += 1