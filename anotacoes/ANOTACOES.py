pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Bruno", "idade": 30},
    {"nome": "Carlos", "idade": 22}
]

# Acessar todos os nomes
for pessoa in pessoas:
    print(pessoa["nome"])

# Acessar apenas o nome da primeira pessoa
print(pessoas[0]["nome"])  # Ana

# Criar uma lista com todos os nomes
nomes = [p["nome"] for p in pessoas]
print(nomes)  # ['Ana', 'Bruno', 'Carlos']
