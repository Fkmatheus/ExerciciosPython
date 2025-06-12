# Operações de multiplicação e divisão com num1 e num2

def multiplica(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

multiplicacao = multiplica(n1, n2)
divisao = divide(n1, n2)

print()
print(f"Resultado da divisão: {divisao}")
print(f"Resultado da multiplicação: {multiplicacao}")