# Crie um programa que pede ao usuário que o mesmo digite um número qualquer, 
# em seguida retorne se esse número é primo ou não, caso não, retorne também quantas vezes esse número é divisível:

n = int(input("Digite um número: "))

divisivel = []

for x in range(n, 1, -1):
    if n != x and n % x == 0:
        divisivel.append(x)

if len(divisivel) > 0:
    print(f"Não é primo, é divisivel por: {divisivel}")
else:
    print("È primo")