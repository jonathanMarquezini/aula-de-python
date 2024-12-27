qtd_linhas = 10
qtd_colunas = 10

linhas = 1

while linhas <= 10:
    colunas = 1
    
    while colunas <= qtd_colunas:
        print(f'{linhas} x {colunas} = {linhas * colunas}')
        colunas += 1
        continue
    
    linhas += 1
    
print("Fim da tabuada")