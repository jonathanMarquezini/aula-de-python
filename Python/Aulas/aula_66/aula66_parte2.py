x = 10

def soma():
    x = 11

    print(x + 1)

    def soma_2():
        soma(x - 2)
    
    soma_2()

soma()