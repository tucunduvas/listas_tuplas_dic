# 68. Converta uma lista de tuplas (chave, valor) em um dicion´ario.

lista = [('1', 1), ('2', 2), ('3', 3)]
lista2 = [{x[0]: x[1]} for x in lista]
print(lista2)