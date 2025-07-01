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

listainversa = lista[::-1]
print(listainversa)

# [('ca', 5.0), ('vi', 3.0), ('ma', 9.0)]

# # 17. Como reverter uma tupla
# # Usando a técnica de fatiamento, podemos reverter a tupla. Uma nova cópia da tupla é criada durante este processo.

# old_tuple = ('M', 'A', 'K', 'E', 'U', 'S', 'E', 'O', 'F')
# print("Old tuple:")
# print(old_tuple)
# # Reversing tuple using slicing
# new_tuple = old_tuple[::-1]
# print("New tuple:")
# print(new_tuple)
# # prints
# # Old tuple:
# ('M', 'A', 'K', 'E', 'U', 'S', 'E', 'O', 'F')
# # New tuple:
# ('F', 'O', 'E', 'S', 'U', 'E', 'K', 'A', 'M')