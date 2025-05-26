minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Criar uma sublista dos elementos de índice 3 até 7 (excluindo o 8)
sublista1 = minha_lista[3:8]
print(sublista1)  # Saída: [4, 5, 6, 7]

# Criar uma sublista com todos os elementos de índice par
sublista2 = minha_lista[::2]
print(sublista2)  # Saída: [1, 3, 5, 7, 9]

# Criar uma sublista com elementos maiores que 5
sublista3 = [elemento for elemento in minha_lista if elemento > 5]
print(sublista3)  # Saída: [6, 7, 8, 9, 10]

# Lista base
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exemplos de sublistas (slicing)
print("lista[2:5]     →", lista[2:5])      # [2, 3, 4]
print("lista[:4]      →", lista[:4])       # [0, 1, 2, 3]
print("lista[5:]      →", lista[5:])       # [5, 6, 7, 8, 9]
print("lista[-3:]     →", lista[-3:])      # [7, 8, 9]
print("lista[::2]     →", lista[::2])      # [0, 2, 4, 6, 8]
print("lista[::-1]    →", lista[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Lista aninhada (matriz)
matriz = [[1, 2], [3, 4], [5, 6]]
print("matriz[1]      →", matriz[1])       # [3, 4] → sublista
print("matriz[1][0]   →", matriz[1][0])    # 3     → elemento da sublista


#sublista = [inicio:fim]