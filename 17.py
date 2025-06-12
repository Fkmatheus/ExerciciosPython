# Dadas duas variáveis num1 e num2 com valores 100 e 89,
#  respectivamente, verifique se o valor de num1 é maior que o de num2:

def verifica_maior(n1, n2):
    if n1 > n2:
        return f'{n1} é o maior número'
    else:
        return f'{n2} é o maior número'


n1 = 100
n2 = 89

print(verifica_maior(n1, n2))