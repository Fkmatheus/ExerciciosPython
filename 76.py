# Escreva um programa, uma calculadora simples de 4 operações, onde o usuário escolherá entre uma das 4 operações 
# (soma, subtração, multiplicação e divisão). 
# Lembrando que o usuário digitará apenas dois valores, e escolherá apenas uma operação matemática do menu.

class Calculadora:
    def soma(n1, n2):
        return n1 + n2
    
    def sub(n1, n2):
        return n1 - n2
    
    def multi(n1, n2):
        return n1 * n2
    
    def div(n1, n2):
         return n1 / n2
    
    def menu():
        n1 = input("Digite o primeiro número: ")
        n1 = int(n1)

        n2 = input("Digite o segundo número: ")
        n2 = int(n2)

        op = input("Que operação deseja realizar? + - * / ")

        if op == '+':
            resultado = Calculadora.soma(n1,n2)
            print(f"O Resultado é: {resultado}")
        
        if op == '-':
            resultado = Calculadora.sub(n1,n2)
            print(f"O Resultado é: {resultado}")

        if op == '*':
            resultado = Calculadora.multi(n1,n2)
            print(f"O Resultado é: {resultado}")

        if op == '/':
            resultado = Calculadora.div(n1,n2)
            print(f"O Resultado é: {resultado}")

Calculadora.menu()