lista1 = [1,2,3,4,5]
lista2 = [1,2,7,8,5]

def inter(lista1, lista2):
    intersecao = (list(set(lista1).intersection(set(lista2))))
    return intersecao

print(f"Os valores que estãp em ambas as listas são: {inter(lista1, lista2)}")