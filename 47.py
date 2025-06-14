# Crie um dicionário usando o construtor de dicionários do Python, 
# alimente os valores do mesmo com os dados de duas listas:

dicio = dict()

chaves = [1,2,3]
valores = ['Ana', 'Matheus', 'Maria']

contador = 0
for x in range(len(chaves)):
    dicio[chaves[contador]] = valores[contador]
    contador += 1

print(dicio)
