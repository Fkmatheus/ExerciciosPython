# Some os valores das variáveis num1 e num2: Sendo num1 = 52 e num2 = 106. Por fim exiba em tela o resultado da soma.

def soma(n1, n2):
    return n1 + n2


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = soma(n1, n2)

print(f"A soma é: {soma}")