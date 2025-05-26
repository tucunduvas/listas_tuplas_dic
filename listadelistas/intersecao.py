conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# União: elementos que estão em A ou B (ou em ambos)
uniao = conjunto_a | conjunto_b

# Interseção: elementos que estão em A e B
intersecao = conjunto_a & conjunto_b

# Diferença: elementos que estão em A mas não estão em B
diferenca = conjunto_a - conjunto_b

# Exibição dos resultados
print("Conjunto A:", conjunto_a)

print("intersecao:", intersecao)
#treinando comits git hub

# Conjuntos de exemplo
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# União - elementos em a OU b
uniao = a | b  # ou a.union(b)

# Interseção - elementos em a E b
intersecao = a & b  # ou a.intersection(b)

# Diferença - elementos em a mas NÃO em b
diferenca = a - b  # ou a.difference(b)

# Diferença simétrica - elementos em a OU b, mas NÃO nos dois
diferenca_simetrica = a ^ b  # ou a.symmetric_difference(b)

