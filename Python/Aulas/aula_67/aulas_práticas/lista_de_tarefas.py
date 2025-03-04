# Requisitos do Exercício:
# O programa deve permitir ao usuário adicionar tarefas, cada tarefa deve ter um ID, um nome e um status (pendente ou concluída).
# O programa deve permitir ao usuário listar todas as tarefas ou apenas as pendentes ou concluídas.
# O programa deve permitir ao usuário marcar uma tarefa como concluída.
# O programa deve permitir ao usuário excluir tarefas.
# O sistema deve ser simples, interativo e utilizar uma lista de dicionários para armazenar as tarefas.

import os

tarefas = []
id = 0

def adicionando_tarefas():
    global id

    print('Lista de tarefas!')

    while True:
        usuario = input("Gostaria de adicionar uma lista? [S] ou [N]: ").strip().lower()

        if usuario == 's':
            id += 1 # cria uma identidade para a tarefa

            pergunta = input('Informe o nome da tarefa: ').strip()

            if pergunta:
                # solicitando os status da tarefa
                while True:
                    status = input('Nos informe os status da tarefa (pendente/concluido): ').strip().lower()

                    if status in ['pendente', 'concluido']:
                        break
                    else:
                        print('Opção inválida')
                
                adicionar_na_lista = {'ID': id, 'Tarefa': pergunta, 'Status': status}
                tarefas.append(adicionar_na_lista)

                print(f'Tarefa "{pergunta}" com status "{status}" adicionado a lista')

        elif usuario == 'n':
            print('Você saiu do sistema...')
            break
        else:
            print('Opção inválida')

def limpar_terminal():
    os.system('cls')

def listar_tarefas():
    pergunta = input('Gostaria de ver algumas de suas tarefas? [S] ou [N]: ').strip().lower()
        
    if pergunta == 'n':
        print('Você saiu do sistema...')
    
    elif pergunta == 's':
        
        if not tarefas:
            print('Lista de tarefas vazias. Saindo do menu...')          

        while True:
            status_tarefas = input('Qual tarefa você gostaria de ver? (todas/pendentes/concluidas), Caso queira sair, digite "exit": ').strip().lower()

            if status_tarefas == 'todas':
                for tarefa in tarefas:
                    print(f"ID: {tarefa['ID']}")
                    print(f"Tarefa: {tarefa['Tarefa'].capitalize()}")
                    print(f"Status: {tarefa['Status'].capitalize()}")  # Deixa a 1ª letra maiúscula
                    print("-" * 30)  # Linha separadora para organização   

            elif status_tarefas == 'pendentes':
                for tarefa in tarefas:
                    if tarefa['Status'] == 'pendente':
                        print(f"ID: {tarefa['ID']}")
                        print(f"Tarefa: {tarefa['Tarefa'].capitalize()}")
                        print(f"Status: {tarefa['Status'].capitalize()}")
                        print('-' * 30)
                    
                    else:
                        print('Não tem tarefas pendentes')
            
            elif status_tarefas == 'concluidas':
                for tarefa in tarefas:
                    if tarefa['Status'] == 'concluido':
                        print(f"ID: {tarefa['ID']}")
                        print(f"Tarefa: {tarefa['Tarefa'].capitalize()}")
                        print(f"Status: {tarefa['Status'].capitalize()}")
                        print('-' * 30)
                    
                    else:
                        print('Não tem tarefas concluidas')

            elif status_tarefas == 'exit':
                print('Você saiu da lista de tarefas...')
                break
            
            else:
                print('Opção inválida')

def modificar_status():
    pergunta = input("Gostaria de fazer alguma alteração nos status de alguma tarefa? [S] ou [N]: ").strip().lower()

    if pergunta == 'n':
        print('Saindo do sistema')
        return

    elif pergunta == 's':
        if not tarefas:
            print('Lista de tarefas vazia!')
            return

        for tarefa in tarefas:
            print('Todas as tarefas!')
            print(f"ID: {tarefa['ID']}")
            print(f"Tarefa: {tarefa['Tarefa'].capitalize()}")
            print(f"Status: {tarefa['Status'].capitalize()}")  
            print("-" * 30)

def modificar_status():
    pergunta = input("Gostaria de fazer alguma alteração nos status de alguma tarefa? [S] ou [N]: ").strip().lower()

    if pergunta == 'n':
        print('Saindo do sistema')
        return

    elif pergunta == 's':
        if not tarefas:
            print('Lista de tarefas vazia!')
            return

        for tarefa in tarefas:
            print('Todas as tarefas!')
            print(f"ID: {tarefa['ID']}")
            print(f"Tarefa: {tarefa['Tarefa'].capitalize()}")
            print(f"Status: {tarefa['Status'].capitalize()}")  
            print("-" * 30)

        while True:
            id_tarefa_input = input('Informe o ID da tarefa que deseja fazer alteração ou "exit" para sair do sistema: ').strip().lower()

            if id_tarefa_input == 'exit':
                print('Saindo do sistema...')
                break

            try:
                id_tarefa = int(id_tarefa_input)  # Tentando converter para int

                tarefa_encontrada = None
                for tarefa in tarefas:
                    if tarefa['ID'] == id_tarefa:
                        tarefa_encontrada = tarefa
                        break

                if tarefa_encontrada is None:
                    print('ID inválido. Tente novamente.')
                    continue

                print(f"Tarefa encontrada: {tarefa_encontrada['Tarefa']}")
                print(f"Status atual: {tarefa_encontrada['Status'].capitalize()}")

                alteracao = input("Informe o novo status (pendente/concluido): ").strip().lower()

                if alteracao not in ['pendente', 'concluido']:
                    print('Status inválido. Status não atualizado.')
                else:
                    tarefa_encontrada['Status'] = alteracao
                    print(f"Status da tarefa '{tarefa_encontrada['Tarefa']}' atualizado para '{alteracao}'.")

            except ValueError:
                print('ID inválido, digite um número válido ou "exit" para sair.')

def excluir_tarefas():
    pergunta = input("Deseja excluir alguma tarefa? [S] ou [N]: ").strip().lower()

    if pergunta == 'n':
        print('Saindo do sistema...')
        return
    
    elif pergunta == 's':
        if not tarefas:
            print('Lista de tarefas vazia!')
            return  # Saída antecipada

        for tarefa in tarefas:
            print('Todas as tarefas!')
            print(f"ID: {tarefa['ID']}")
            print(f"Tarefa: {tarefa['Tarefa'].capitalize()}")
            print(f"Status: {tarefa['Status'].capitalize()}")  
            print("-" * 30)

        while True:
            try:
                id_tarefa_input = input("Informe o ID da tarefa que deseja excluir ou 'exit' para sair do sistema: ").strip().lower()

                # Verificando se o usuário digitou 'exit'
                if id_tarefa_input == 'exit':
                    print('Saindo do sistema...')
                    break

                id_tarefa = int(id_tarefa_input)  # Tentando converter para int

                excluir_tarefa = None

                for tarefa in tarefas:
                    if tarefa['ID'] == id_tarefa:
                        excluir_tarefa = tarefa
                        break
                
                if excluir_tarefa is None:
                    print('ID inválido, tente novamente')
                    continue

                # Exibindo tarefa encontrada
                print(f'Tarefa encontrada: {excluir_tarefa["Tarefa"]}')
                print(f'ID: {excluir_tarefa["ID"]}, Status: {excluir_tarefa["Status"].capitalize()}')

                excluir = input('Deseja excluir essa tarefa? [S] ou [N]: ').strip().lower()

                if excluir == 's':
                    tarefas.remove(excluir_tarefa)
                    print(f'Tarefa "{excluir_tarefa["Tarefa"]}" excluída com sucesso!')

                    print('Lista de tarefas atualizada:')
                    for i in tarefas:
                        print(f"ID: {i['ID']}")
                        print(f"Tarefa: {i['Tarefa'].capitalize()}")
                        print(f"Status: {i['Status'].capitalize()}")  
                        print("-" * 30)

                elif excluir == 'n':
                    print('Saindo da exclusão de tarefas...')
                    break
                else:
                    print('Opção inválida, tente novamente')

            except ValueError:
                print("ID inválido, digite um número válido.")

adicionando_tarefas()
limpar_terminal() # limpa o terminal
listar_tarefas()
limpar_terminal() # limpa o terminal
modificar_status()
limpar_terminal() # limpa o terminal
excluir_tarefas()

"""
Resumo: exercício bem complexo (pra mim), mas concluído com sucesso
70 % feito por mim
30 % feito pelo CHATGPT (refatorando e dando dicas de melhoria)
"""