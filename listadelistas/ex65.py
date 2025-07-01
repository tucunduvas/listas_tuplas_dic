# 65. Fa¸ca um programa que recebe nomes de alunos e suas idades. Armazene usando
# uma lista de tuplas e depois transforme em dicion´ario.

lista = []
while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    if nome == 'sair' and idade == 0:
        break
    pessoa = nome,idade
    lista.append(pessoa)
    print(lista)
    # list2 = [{x[0]: x[1]} for x in lista]
    dic = {}
    list2 = [{'nome': x[0], 'idade': x[1]} for x in lista]
print(list2)