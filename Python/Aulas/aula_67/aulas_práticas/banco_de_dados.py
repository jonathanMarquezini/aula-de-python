# Meta: Criar Nome e senha para o usuário, jogar em uma lista e deixá-lo visualizar caso acerte a senha criada

import os

registros = []
id = 0  # Contador de ID

CEO = '123'  # Senha para visualizar todos os dados do banco de dados

def usuario():
    global id
    
    while True:
        pergunta = input("Gostaria de fazer um cadastro? [S] ou [N]: ").strip().lower()

        if pergunta == 's':
            id += 1  # Incrementa o ID para cada novo usuário
            nome = input("Me informe o seu nome e sobrenome: ").strip().lower()

            if nome:
                print(f'Nome: {nome}, Adicionado!')
                
                def senha():
                    print('Agora que você nos indicou o seu nome, está na hora de criar uma senha!')
                    
                    while True:
                        criando_senha = input('Crie uma senha (Mínimo de 8 caracteres): ').strip().lower()
                        verificando_senha = input("Confirme a sua senha: ").strip().lower()

                        if verificando_senha == criando_senha and len(criando_senha) >= 8:
                            registros.append({"id": id, "nome": nome, "senha": criando_senha})
                            print(f'Usuário cadastrado com sucesso!')
                            break  
                        else:
                            print('Senha incorreta ou número de caracteres insuficiente. Tente novamente.')

                senha()
            
            else:
                print('Campo vazio!')

        elif pergunta == 'n':
            print('Saindo do sistema...')
            break  

        else:
            print('Opção inválida')

def limpar_terminal():
    os.system('cls')

def banco_de_dados():
    while True:
        pergunta = input("Deseja visualizar os dados do banco de dados? [S] ou [N]: ").strip().lower()

        if pergunta == 's':
            usuario = input("Você é um Usuário ou Adm? ").strip().lower()

            if usuario == 'usuario':  # Acesso do usuário
                senha_digitada = input("Digite a sua senha: ").strip().lower()

                usuario_encontrado = None
                for registro in registros:
                    if registro["senha"] == senha_digitada:
                        usuario_encontrado = registro
                        break  

                if usuario_encontrado:
                    print("\nUsuário localizado!")
                    print(f"{usuario_encontrado['id']}, {usuario_encontrado['nome']}, {usuario_encontrado['senha']}\n")
                else:
                    print("Senha incorreta ou usuário não encontrado!")

            elif usuario == 'adm':  # Acesso do admin/CEO
                pergunta_adm = input("Deseja visualizar todos os dados? [S] ou [N]: ").strip().lower()

                if pergunta_adm == 's':
                    senha_adm = input("Digite a senha de adm: ").strip().lower()

                    if senha_adm == CEO:
                        print("\nLista de todos os usuários cadastrados:")
                        for registro in registros:
                            print(f"{registro['id']}, {registro['nome']}, {registro['senha']}")
                        print()
                    else:
                        print("Senha incorreta!")  

                elif pergunta_adm == 'n':
                    print('Saindo do sistema, até mais...')
                    break  

                else:
                    print('Opção inválida')

            else:
                print('Opção inválida!')

        elif pergunta == 'n':
            print('Saindo do sistema, até mais...')
            break
        else:
            print('Opção inválida!')

usuario()
limpar_terminal()
banco_de_dados()

"""
Resumo: exercício um pouco mais complexo, mas concluído com sucesso
80 % feito por mim
20 % feito pelo CHATGPT (refatorando e dando dicar de melhoria)
"""