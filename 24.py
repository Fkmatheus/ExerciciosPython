# Crie duas variáveis com dois valores numéricos inteiros digitados pelo usuário, 
# caso o valor do primeiro número for maior que o do segundo, exiba em tela uma mensagem de acordo, 
# caso contrário, exiba em tela uma mensagem dizendo 
# que o primeiro valor digitado é menor que o segundo:

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

def verifica(n1, n2):
    if n1 > n2:
        return 'Estou de acordo'
    else:
        return 'O segundo número é menor do que o primeiro!'
    

print(verifica(n1,n2))