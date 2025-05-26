lista = list()

while True:
    numero = int(input("Digite um número, se digitar -1 o programa para: "))
    if numero == -1:
        break
    lista.append(numero)
    qntd = 0
    soma = 0
    media = 0
    for i in lista:
        qntd += 1
        soma += i
media = soma/qntd
print(lista)
print(media)