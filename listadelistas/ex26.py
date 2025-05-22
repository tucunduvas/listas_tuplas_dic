"""
26. Inverta os elementos de uma lista sem usar o m´etodo reverse.
27. Simule uma pilha usando append e pop. Mostre a pilha a cada opera¸c˜ao.
28. Crie uma fun¸c˜ao que receba uma lista e retorne a soma de todos os elementos
num´ericos.
29. Crie um menu interativo que permita adicionar, remover, listar ou sair de um programa que manipula listas.
"""

lista = [1,2,3,4,5]
qntd = len(lista)

for i in range(0,qntd):
    ultimo_elemento = lista.pop()
    lista.insert(i,ultimo_elemento)
    
print(lista)

