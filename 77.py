# Crie uma função que 
# recebe um número e retorna o mesmo dividido em duas metades, sendo cada metade um elemento de uma lista:

def metade(n):
    return [n//2, n-n//2]


n = int(input("Digite um número: "))

print(metade(n))