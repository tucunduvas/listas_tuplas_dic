# 61. Crie um dicion´ario onde as chaves s˜ao nomes de pessoas e os valores s˜ao listas com
# trˆes notas. Calcule a m´edia de cada aluno.


pessoas = {'gabi': [3,10,7], 'amanda': [7,8,9], 'victor': [10,6,8]}

for nome, notas in pessoas.items():
    media = sum(notas) / len(notas)
    print(f"{nome}: média = {media}")


maior_media = 0
melhor_aluno = ""

for nome, notas in pessoas.items():
    media = sum(notas) / len(notas)
    if media > maior_media:
        maior_media = media
        melhor_aluno = nome

print(f"\nAluno com maior média: {melhor_aluno} ({maior_media:.2f})")
