lista = [1,1,3,3,3,3,6,6,6,6,6,7,7,7,7]

qntd = {}
def contar(lista):
    for i in lista:
        if i in qntd:
            qntd[i] += 1
        else:
            qntd[i] = 1 
    return qntd

contador = contar(lista)

for i,j in contador.items():
    print(f"O número {i} aparece {j} vezes")
    
    