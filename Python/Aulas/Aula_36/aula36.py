usuario = "Jonathan Marquezini"

i = 0

while i < len(usuario):
    string = usuario[i]
    
    print(string)
    
    if string == " ":
        break
    
    i += 1
else:
    # com o break "ativado" o else nunca irá funcionar
    print("Fora do while")
    
print("Fora do laço while")