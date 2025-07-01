"""

46. Implemente a ordena¸c˜ao manual de uma lista usando o algoritmo Bubble Sort.
47. Solicite notas de alunos e armazene como tuplas (nome, nota). Ordene a lista pela
nota em ordem decrescente.
48. Dada uma lista de n´umeros, retorne uma nova lista com os elementos ao quadrado,
mas somente os pares.
49. Implemente uma fun¸c˜ao que gire os elementos de uma lista N posi¸c˜oes para a direita.
50. Crie uma lista de tupla

"""

lista = [1,2,3,4,5,6,7,8,9,10]

listapar = [x**2 for x in lista if x%2==0]

print(listapar)