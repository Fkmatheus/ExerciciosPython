# Crie um programa que lê um valor de início e um valor de fim, 
# exibindo em tela a contagem dos números dentro desse intervalo.

inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))

def contador(inicio, fim):
    for x in range(inicio, fim + 1):
        print(x)


contador(inicio, fim)