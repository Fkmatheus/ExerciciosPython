# Crie um programa que recebe dados de um aluno como nome e suas notas em supostos 3 trimestres de aula, 
# retornando um novo dicionário com o nome do aluno e a média de suas notas:

nome = input("Digite o nome do aluno: ")
nota_primeiro_trimestre = float(input("Digite a nota do primeiro trimestre: "))
nota_segundo_trimestre = float(input("Digite a nota do segundo trimestre: "))
nota_terceiro_trimestre = float(input("Digite a nota do terceiro trimestre: "))

media = (nota_primeiro_trimestre + nota_segundo_trimestre + nota_terceiro_trimestre) / 3

print(f""" 
    Nome do aluno: {nome}
    Notas: {nota_primeiro_trimestre}, {nota_segundo_trimestre}, {nota_terceiro_trimestre}
    Média: {media}
""")