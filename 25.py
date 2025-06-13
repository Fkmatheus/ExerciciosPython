# Peça para que o usuário digite um número, 
# em seguida exiba em tela uma mensagem dizendo se tal número é PAR ou se é ÍMPAR:

n = int(input("Digite um número: "))

def verifica(n):
    if n % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

print(verifica(n))