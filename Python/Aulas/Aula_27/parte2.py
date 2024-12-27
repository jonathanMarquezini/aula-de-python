velocidade_carro = 59
local_carro = 95

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

condicao_1 = velocidade_carro > RADAR_1
condicao_2 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and condicao_1

if condicao_1:
    print("velocidade do carro passou no radar 1")
else: 
    print("velocidade do carro está no radar 1")
    
if condicao_2 and condicao_1:
    print("o carro foi multado no radar 1")
else: 
    print("o carro não foi multado no radar 1")