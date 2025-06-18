# Escreva um programa que encontre todos os números que são divisíveis por 7, 
# mas que não são múltiplos de 5, entre 2000 e 2200 (ambos incluídos). 
# Os números obtidos devem ser impressos em sequência, separados por vírgula e em uma única linha:

n = ""
for x in range(2000, 2200):
    if x % 7 == 0 and x % 5 != 0:
        x = str(x)
        n += f', {x}'

print(n)
