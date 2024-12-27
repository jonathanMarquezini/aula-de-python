nome = input("Digite o seu nome: ")

while True:
    try:
        verificacao_voto = input("Digite a sua idade: ")
        conversao_voto = int(verificacao_voto)
        break
    except ValueError:
        print("Valor inválido! Por favor, digite apenas números: ")
    
if conversao_voto >= 18:
    print(f'{nome}, após uma análise, verifiquei que você já é maior de idade, por isso seu voto é obrigatório')
elif conversao_voto >= 16 and conversao_voto <= 18:
    print(f'{nome}, após uma análise, verifiquei que você tem entre 16/17 anos, por isso seu voto é opcional ')
else:
    print(f'{nome}, após uma análise, verifiquei que você é menor de idade, então você não pode votar')

print("Fim do sistema, caso queira fazer uma nova verificação, clique no botão RUN")