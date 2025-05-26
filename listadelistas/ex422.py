lista = [1,1,3,3,3,3,6,6,6,6,6,7,7,7,7]

qntd = {}
for i in lista:
    if i in qntd:
        qntd[i] += 1
    else:
        qntd[i] = 1 

for i,j in qntd.items():
    print(f"O número {i} aparece {j} vezes")
    