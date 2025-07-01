# 64. Crie um dicion´ario que mapeia n´umeros de 1 a 5 para seus quadrados, usando la¸co
# for.

dic = { }

for i in range(1,6):
    dic[i] = i**2
    
print(dic)