"""
21. Solicite ao usu´ario 10 n´umeros, armazene em uma lista e remova todos os n´umeros
pares usando remove.
22. Crie uma fun¸c˜ao que recebe uma lista e retorna uma nova lista com apenas os
elementos ´unicos.
23. Dada uma lista com nomes duplicados, elimine os nomes repetidos mantendo a
ordem.
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
impares = list()
for i in range(10):
    num = int(input("Digite 10 números: "))
    impares.append(num)

    
for elemento in impares:
    if elemento%2==0:
        impares.remove(elemento)  
        
print(impares)