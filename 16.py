# Escreva um programa que pede que o usuário dê entrada em dois valores, 
# em seguida, exiba em tela o resultado da soma, subtração, multiplicação e divisão desses números:

class Calculadora:
    def somar(n1, n2):
        return n1 + n2
    
    def subtrair(n1, n2):
        return n1 - n2
    
    def multiplicar(n1, n2):
        return n1 * n2
    
    def dividir(n1, n2):
        return n1 / n2
    
    def calcula():
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        print(f""" 
            A soma dos valores é: {Calculadora.somar(n1,n2)}
            A subtração dos valores é: {Calculadora.subtrair(n1,n2)}
            A multiplicação dos valores é: {Calculadora.multiplicar(n1,n2)}
            A divisão dos valores é: {Calculadora.dividir(n1,n2)} 

""")



Calculadora.calcula()