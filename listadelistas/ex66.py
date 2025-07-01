# 66. Dado um dicion´ario com frutas como chave e quantidades como valor, atualize os
# estoques com base em uma lista de vendas.

dic = {'beterraba': 6, 'mamão': 9, 'morango': 15, 'maça': 20}
lista_vendas = [('beterraba', 5), ('mamão', 3), ('morrango', 5), ('maça', 10)]
lista = [{x[0]: x[1]} for x in lista_vendas]

# for i,j in dic.items():
#     for x in lista:
#         for chave, valor in x.items():
#             if i == chave:
#                 total = j-valor 
#                 j = total
# print(dic)

for x in lista:
    for chave, valor in x.items():
        if chave in dic:
            dic[chave] -= valor

print(dic)