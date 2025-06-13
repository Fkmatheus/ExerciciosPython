# Crie um programa que realiza a Progressão Aritmética de 20 elementos, 
# com primeiro termo e razão definidos pelo usuário:

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))

progressao = []

soma = termo

for x in range(20):
    progressao.append(soma)
    soma += razao

print(progressao)