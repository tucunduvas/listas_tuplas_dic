lista = [1,2,4,6,5]
verifica_lista_ordenada = 0

def verifica_lista_ordenada(lista):
    lista_ordenada = lista.sort()
    if lista == lista_ordenada:
        print("A lista está ordenada")
    else: 
        print("A lista não está ordenada")
        
print(verifica_lista_ordenada(lista))