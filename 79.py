# Defina uma função que pode aceitar duas strings como entrada, exibindo em tela apenas a string de
#  maior tamanho/comprimento. Caso as duas strings tenham mesmo tamanho, exiba em tela as duas:

def string_maior(s1, s2):
    if len(s1) == len(s2):
        print(s1)
        print(s2)
    elif len(s1) > len(s2):
        print(s1)
    else:
        print(s2)

s1 = input("Digite a primeira frase: ")
s2 = input("Digite a segunda frase: ")

string_maior(s1,s2)
    