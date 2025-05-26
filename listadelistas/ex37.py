lista = ['ama', 'creme', 'brigadeiro', 'rua', 'pingo', 'ju']

for i in lista:
    if len(i)<4:
        lista.remove(i)
            
print(lista)