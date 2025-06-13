# Verifique se o valor de num1 consta nos elementos 
# de lista1. Sendo num1 = 100 e lista1 = [10, 100, 1000, 10000, 100000].

lista = [10, 100, 1000, 10000, 100000]

num1 = 100

def verifica_se_existe(lista,num):
    return num in lista



print(verifica_se_existe(lista,num1))