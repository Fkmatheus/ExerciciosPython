# Crie um programa que pede que o usuário digite um nome ou uma frase, 
# verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.

frase = input("Digite uma frase: ")

frase_ao_contrario = ""

contador = 0
quantidade_de_letras = len(frase)
i = -1

while contador < quantidade_de_letras:
    frase_ao_contrario += frase[i]
    if contador < quantidade_de_letras:
        i = i - 1
        contador += 1

if frase == frase_ao_contrario:
    print("È um palindromo")
else:
    print("Não é um palindromo")