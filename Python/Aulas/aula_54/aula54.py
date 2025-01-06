lista = [] 
indice = 0 

print('----- LISTA DE COMPRAS/AFAZERES -----')

while True:
    print("\nEscolha uma das opções abaixo:")
    print("1. Adicionar")
    print("2. Deletar")
    print("3. Limpar")
    print("4. Visualizar")
    print("5. Sair")
    
    usuario = input("Informe uma opção (1 - 5): ")
    
    print('-' * 20)
    
    if usuario == '1':
        
        adicionar_valor = input("Digite o nome do item: ").lower()
        
        if adicionar_valor in lista:
            print(f'Você já adicionou esse item "{adicionar_valor}" na lista')
            print(lista)
        else:
            lista.insert(indice ,adicionar_valor)
            print(lista)
        
        indice += 1
    elif usuario == '2':
        if not lista:
            print("A lista está vazia, nada para deletar.")
        else:
            print("Itens na lista:")
            for i, item in enumerate(lista, 1):
                print(f"{i}. {item}")
            
            try:
                deletar_indice = int(input("Qual item deseja deletar? Informe o número correspondente: ")) - 1
                if 0 <= deletar_indice < len(lista):
                    deletado = lista.pop(deletar_indice)
                    print(f'Item "{deletado}" excluído.')
                else:
                    print("Índice inválido. Nenhum item foi excluído.")
            except ValueError:
                print("Por favor, insira um número válido.")
            
    elif usuario == '3':
        print(lista)
        
        limpar = input("Deseja limpar a lista? (sim/não): ").lower()
        
        if limpar == 'sim':
            lista.clear()
            print(f'lista {lista} vazia')
    
    elif usuario == '4':
        
        if lista:
            print(f'Itens na lista: {lista}')
        else:
            print('A lista está vazia')
            
    elif usuario == '5':
        print('Você saiu do sistema')
        break
           
    else:
        print('Opção inválida, tente novamente!')
        continue