# lower(), startswith(), endswith(), strip()

nome = input("Digite o seu nome: ").lower() # converte letras maiúsculas para minúsculas
print(nome)

# startswith(), endswith()

usuario = input("Digite o seu primeiro nome: ").lower()

if usuario.startswith('a'): # começa com
    print("seu nome começa com A") 
elif usuario.endswith('a'): # termina com
    print("seu nome termina com A")
    
# strip()

digite = input("Digite alguma frase qualquer: ").strip() # remove espaços em branco extras

print(f'você digitou: {digite}')