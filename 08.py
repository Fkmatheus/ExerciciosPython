# 8 - Peça para que o usuário digite um número, em seguida o converta para float, 
# exibindo em tala tanto o número em si quanto seu tipo de dado.

def pega_numero():
    numero = input("Digite um número: ")
    return numero

def converte_float(numero):
    numero = float(numero)
    return numero

def mostra_valores(numero):
    print(numero)
    print(type(numero))

mostra_valores(converte_float(pega_numero()))