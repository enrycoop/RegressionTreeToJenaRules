""" quadrati = []
for n in range(10):
    quadrati.append(n**2)
print(quadrati) """

quadrati = [n**2 for n in range(10)]
print(quadrati)

lista1 = [1,2,3]
lista2 = [3,1,4]
""" 
mix = []

for x in lista1:
    for y in lista2:
        if x != y:
            mix.append((x,y)) """

mix =[(x,y) for x in lista1 for y in lista2 if x!=y]
print(mix)

stringati = [str(n) for n in lista1]
print(stringati)