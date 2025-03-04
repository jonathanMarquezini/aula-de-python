# escopo_global = 1

# def escopo_local():
#     # x = 1
#     # print(x)
#     print(escopo_global)

# escopo_local()

x = 1

def teste():
    print(x)

    def soma():
        y = 1
        y += x
        print(y)

    soma()

teste()