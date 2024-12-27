print(str(1), type(str(1))) # int que virou string

print(int("1"), type(int("1"))) # string que virou int

print(int(1.1), type(int(1.1))) # float que virou int

print(float(1), type(float(1))) # int que virou float

a = 0
b = 1

print(bool(a), type(bool(a))) # int que virou boolean
print(bool(b), type(bool(b))) # int que virou boolean

c = True
d = False

print(int(c), type(int(c))) # boolean que virou int
print(float(d), type(float(d))) # boolean que virou float

texto = "1"

# Fazendo a conversão de tipos de dados + soma de valores

print(float(texto) + 1, type(float(texto))) # str que virou float
print(int(texto) + 2, type(int(texto))) # str que virou int