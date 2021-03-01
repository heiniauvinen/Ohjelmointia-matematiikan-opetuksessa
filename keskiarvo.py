lista = []
for i in range(3):
    luku = float(input("Anna luku: "))
    lista.append(luku)

def keskiarvo(lista):
    summa=0
    for i in range(3):
        summa = summa + lista[i]
    return summa/3

print(keskiarvo(lista))


    
