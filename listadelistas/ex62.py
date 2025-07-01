# 62. Crie uma lista de dicion´arios com nome, idade e cidade. Imprima os dados de cada
# pessoa.

lista = [{'nome': 'Gabi', 'idade': 18, 'cidade': 'Castilho'},
        {'nome': 'Ale', 'idade': 19, 'cidade': 'Sao Paulo'},
        {'nome': 'Padre', 'idade': 28, 'cidade': 'Castelo Branco'}]

for i in lista:
    print (i['nome'])
    print(i['idade'])
    print(i['cidade'])
    print( '-'*30)