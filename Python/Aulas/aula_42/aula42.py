# continue, break, else, etc

for i in range(10):
    
    if i == 2:
        print("'i' é 2 pulando...")
        continue
        
    if i == 8:
        print("'i' é 8, seu else não será executado")
        break
        
    for j in range(1, 3): # exibindo a linha e a coluna
        print(i, j)
        
else:
    print("Loop finalizado")    