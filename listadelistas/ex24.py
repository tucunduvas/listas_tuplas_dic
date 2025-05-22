"""
24. Separe uma lista de n´umeros em duas: uma com pares e outra com ´ımpares.
25. Solicite uma frase ao usu´ario e retorne uma lista com todas as palavras (use split).
26. Inverta os elementos de uma lista sem usar o m´etodo reverse.
27. Simule uma pilha usando append e pop. Mostre a pilha a cada opera¸c˜ao.
28. Crie uma fun¸c˜ao que receba uma lista e retorne a soma de todos os elementos
num´ericos.
29. Crie um menu interativo que permita adicionar, remover, listar ou sair de um programa que manipula listas.

# 3. O código não tem validação de entrada
# - Não verifica se o input é realmente um número inteiro

# 2. A verificação de número ímpar (n%2!=0) está dentro do loop, o que é ineficiente e pode
# levar a resultados incorretos.
"""

lista = [1,2,3,4,5,6,7,8,9,10]
listapares = list()
listaimpares = list()
for elemento in lista:
    if elemento%2==0:
        listapares.append(elemento)
    else: 
        listaimpares.append(elemento)

print(f"lista pares: {listapares}")
print(f"lista ímpares: {listaimpares}")

