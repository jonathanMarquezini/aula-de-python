# if / elif / else
# se / se não se / se não 

sistema = input("Você quer [E]ntrar ou [S]air do sistema? ")

if sistema == 'E' or sistema == 'e':
    print("Você entrou no sistema!")
elif sistema == 'S' or sistema == 's':
    print("Você saiu do sistema")
else:
    print("Não entendi a sua opção, fim do sistema...")
    
print("Fora dos blocos")