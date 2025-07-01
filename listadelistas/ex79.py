from functools import reduce

""" 
Some todos os números da lista abaixo usando reduce:

numeros = [10, 20, 30, 40]
Multiplique todos os elementos da lista abaixo usando reduce:

python
Copiar
Editar
valores = [2, 3, 5]
Use reduce para transformar uma lista de strings em uma frase única:

python
Copiar
Editar
palavras = ["Python", "é", "muito", "legal"]
🟡 Intermediário
Use reduce para encontrar o menor número em uma lista:

python
Copiar
Editar
lista = [34, 12, 88, 5, 67]
Some apenas os números ímpares da lista abaixo usando reduce:

python
Copiar
Editar
numeros = [1, 2, 3, 4, 5, 6, 7]
Use reduce para contar quantas vezes cada letra aparece em uma palavra (retorne um dicionário):

python
Copiar
Editar
palavra = "abacate"
🔴 Avançado
Dada a lista de dicionários, use reduce para somar todos os salários:

python
Copiar
Editar
funcionarios = [
    {"nome": "João", "salario": 2000},
    {"nome": "Maria", "salario": 2500},
    {"nome": "Ana", "salario": 2200}
]
Use reduce para transformar uma lista de pares chave-valor em um dicionário:

python
Copiar
Editar
pares = [("nome", "Carlos"), ("idade", 30), ("cidade", "Recife")]
Dada a lista de listas, use reduce para achatá-la (transformar em uma lista única):

python
Copiar
Editar
listas = [[1, 2], [3, 4], [5, 6]]
Dado o texto abaixo, use reduce para contar quantas palavras ele tem (considere que as palavras estão separadas por espaços):

python
Copiar
Editar
texto = "A linguagem Python é versátil e poderosa"
"""

# Some todos os números da lista abaixo usando reduce:

numeros = [10, 20, 30, 40]

resultado = reduce(lambda x,y: x+y, numeros)
print(resultado)

valores = [2, 3, 5]
resultado = reduce(lambda x, y: x*y, valores)
print(valores)
# Use reduce para transformar uma lista de strings em uma frase única:

palavras = ["Python", "é", "muito", "legal"]

frase = reduce(lambda x,y: x+y, palavras )
print(frase)


lista = [34, 12, 88, 5, 67]
# Some apenas os números ímpares da lista abaixo usando reduce:

soma = reduce(lambda acumulador,y: acumulador+y if y%2!=0 else acumulador , lista, 0)
print(soma)

# Use reduce para contar quantas vezes cada letra aparece em uma palavra (retorne um dicionário):

palavra = 'abacate'
dic = {}
def vezes(acumulador, string):
    dic[string] = len(acumulador)
    return dic
    
    
resultado = reduce(vezes, palavra)

print(resultado)
