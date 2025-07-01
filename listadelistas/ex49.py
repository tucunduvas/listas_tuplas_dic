"""

46. Implemente a ordena¸c˜ao manual de uma lista usando o algoritmo Bubble Sort.
47. Solicite notas de alunos e armazene como tuplas (nome, nota). Ordene a lista pela
nota em ordem decrescente.
48. Dada uma lista de n´umeros, retorne uma nova lista com os elementos ao quadrado,
mas somente os pares.
49. Implemente uma fun¸c˜ao que gire os elementos de uma lista N posi¸c˜oes para a direita.
50. Crie uma lista de tupla

"""
n = int(input("digite quantas posicoes você quer que gire a direita: "))
# lista = [1,2,3,4,5]
# lista2 = [1,2,3,4,5]

def girar_direita(lista, n):
    lista2 = lista[:]
    j = 1
    k = 0
    for i in range(0,n):
        lista[i] = lista2[-j]
        lista[-j] = lista2[k]
        j += 1
        k +=1
    print(lista)

    
girar_direita(['a','b','c', 'd'], n)

