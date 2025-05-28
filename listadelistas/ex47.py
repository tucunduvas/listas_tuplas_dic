"""

46. Implemente a ordena¸c˜ao manual de uma lista usando o algoritmo Bubble Sort.
47. Solicite notas de alunos e armazene como tuplas (nome, nota). Ordene a lista pela
nota em ordem decrescente.
48. Dada uma lista de n´umeros, retorne uma nova lista com os elementos ao quadrado,
mas somente os pares.
49. Implemente uma fun¸c˜ao que gire os elementos de uma lista N posi¸c˜oes para a direita.
50. Crie uma lista de tupla

"""
lista = list()
while True:
    print("Para sair digite -1: ")
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    if nome == -1 or nota == -1: 
        break
    tupla = ( nome, nota)
    lista.append(tupla)

for i,j in lista:
    print(i)
    
