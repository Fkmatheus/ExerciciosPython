# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, ao final do processo 
# exiba em tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma dos mesmos:

impars = 0
soma = 0

for x in range(100):
    if x % 2 == 1:  
        soma += x
        impars += 1

print(f"Soma dos números impares: {soma}")
print(f"Quantidade de números impares: {impars}")