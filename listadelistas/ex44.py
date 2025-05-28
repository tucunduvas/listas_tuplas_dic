lista = [1,2,3,4,5,6,7,8]
listadesubs = []
divisao = 2

for i in (0,len(lista),divisao):
    sublista = lista[i:i+divisao]
    listadesubs.append(sublista)
    
print(listadesubs)