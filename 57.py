# Crie uma função com dois parâmetros relacionados ao nome e sobrenome de uma pessoa, 
# a função deve retornar uma mensagem de boas-vindas e esses dados devem ser digitados pelo usuário:

def nome_completo(nome,sobrenome):
    print(f"Bem vindo! {nome} {sobrenome}")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo(nome,sobrenome)