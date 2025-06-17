# Crie uma função de número de parâmetros indefinido, 
# que realiza a soma dos números repassados como parâmetro, independentemente da quantidade de números:

def soma_numeros(*args):
    soma = list(args)
    soma = sum(soma)
    return soma

resultado = soma_numeros(2,2,4,5,10,11)
resultado2 = soma_numeros(42,56,333,5,10,112)

print(resultado)
print(resultado2)
