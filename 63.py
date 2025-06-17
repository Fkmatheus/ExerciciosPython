""" Escreva um programa que retorna o número de Fibonacci: Sendo o número de 
Fibonacci um valor iniciado em 0 ou em 1 onde cada termo subsequente corresponde
 à soma dos dois anteriores."""

def fibonacci(n):
    sequencia = [0, 1]

    q = 1

    for x in range(n):
        sequencia.append(sequencia[q] + sequencia[q - 1])
        q += 1
    
    return sequencia

n = int(input("Quantidade de números: "))

fibo = fibonacci(n)

print(fibo)

    