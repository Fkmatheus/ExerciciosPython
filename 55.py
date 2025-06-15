# Crie uma função que recebe um nome como parâmetro e exibe em tela uma mensagem de boas-vindas. 
# O nome deve ser fornecido pelo usuário, incorporado na mensagem de boas-vindas da função:

def pede_nome():
    nome = input("Digite seu nome: ")
    return nome

def mensagem(nome):
    print(f"Olá! {nome}")

nome = pede_nome()

mensagem(nome)