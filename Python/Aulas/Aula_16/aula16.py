idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print('Você ja pode Votar')
elif idade >= 16 and idade < 18:
    print('Voto opcional')
else:
    print('Você é menor de idade e não pode votar')