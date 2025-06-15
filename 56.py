# Crie uma função que recebe um valor digitado pelo usuário e eleva esse valor ao quadrado:

def eleva_ao_quadrado(n):
    return n ** 2

def recebe_valor():
    n = input("Digite um número: ")
    n = int(n)
    return n

numero = recebe_valor()

print(eleva_ao_quadrado(numero))