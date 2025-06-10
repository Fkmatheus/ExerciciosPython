# 5 - Crie uma variável nome e atribua para a mesma um nome digitado pelo usuário:


def registra_nome():
    nome = input("Digite seu nome: ")
    return nome

def mostrar_nome(nome):
    print(nome)


mostrar_nome(registra_nome())