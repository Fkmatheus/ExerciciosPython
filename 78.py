# Crie um programa que gera um dicionário a partir de um valor digitado pelo usuário, 
# de modo que serão exibidos todos valores antecessores a este número multiplicados por eles mesmos. 
# Supondo que o usuário tenha digitado 4, a saída deve ser {1: 1, 2: 4, 3: 9, 4: 16}

n = int(input("Digite um número: "))

dic = {}

for x in range(n):
    dic[x + 1] = (x + 1) * (x + 1)


print(dic)