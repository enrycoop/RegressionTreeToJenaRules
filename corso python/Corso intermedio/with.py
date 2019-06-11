""" zenigata = open("zaza.txt",'r')
for riga in zenigata:
    print(riga)

zenigata.close() """

with open("zaza.txt",'r') as zen:
    for riga in zen:
        print(riga)

print(zen.closed) 
""" 
numeri = []
dati = open('zaza.txt','r')
try:
    for num in dati:
        numeri.append(float(num))
except:
    print("quel maledetto lupin!")
finally:
    dati.close() """
numeri = []
with open("zaza.txt",'r') as dati:
    try:
        for num in dati:
            numeri.append(float(num))
    except ValueError:
        pass
print(dati.closed)