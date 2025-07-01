# 70. Crie um dicion´ario que associa cada letra de uma palavra `a sua posi¸c˜

lista = ['para', 'cinco', 'ovo']
dic = {}
for i in lista:
    lista2 =[ {x, j} for x,j in enumerate(i) ]
    dic[i] = lista2
    
print(dic)

    
        