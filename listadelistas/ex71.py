
alunos = [
    ("Ana", 8.0, 7.5, 9.0),
    ("Bruno", 6.0, 5.5, 6.5),
    ("Carla", 9.5, 9.0, 8.5),
    ("Daniel", 7.0, 6.5, 7.5)
]


medias = list(map(lambda aluno: round((aluno[1] + aluno[2] + aluno[3]) / 3, 2), alunos))

aprovados = list(map(lambda aluno: aluno[0],
                    filter(lambda aluno: (aluno[1] + aluno[2] + aluno[3]) / 3 >= 7.0, alunos)))

# Lista de alunos (nome, nota_matematica, nota_portugues, nota_ciencia)
alunos = [
    ("Ana", 8.0, 7.5, 9.0),
    ("Bruno", 6.0, 5.5, 6.5),
    ("Carla", 9.5, 9.0, 8.5),
    ("Daniel", 7.0, 6.5, 7.5)
]

# Calcula a média de cada aluno, arredondando para 2 casas decimais
medias = list(map(lambda aluno: round((aluno[1] + aluno[2] + aluno[3]) / 3, 2), alunos))

# -----------------------------------------------
# LÓGICA DETALHADA DOS APROVADOS:

# filter(...) => filtra os alunos cuja média é >= 7.0
#   lambda aluno: (aluno[1] + aluno[2] + aluno[3]) / 3 >= 7.0
#   Isso verifica se a média das 3 notas é maior ou igual a 7.0
#
# Exemplo: 
#   Para ("Ana", 8.0, 7.5, 9.0) → (8.0 + 7.5 + 9.0)/3 = 8.17 → fica
#   Para ("Bruno", 6.0, 5.5, 6.5) → (6.0 + 5.5 + 6.5)/3 = 6.0 → sai
#
# Depois, usamos map(...) para pegar apenas os nomes (índice 0 da tupla)
#   lambda aluno: aluno[0]
# -----------------------------------------------

# Cria lista com nomes dos alunos aprovados
aprovados = list(map(lambda aluno: aluno[0],
                    filter(lambda aluno: (aluno[1] + aluno[2] + aluno[3]) / 3 >= 7.0, alunos)))

# Exibe os resultados
print("Médias dos alunos:", medias)
print("Alunos aprovados:", aprovados)

