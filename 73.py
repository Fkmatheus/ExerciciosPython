# Crie uma calculadora simples de 4 operações (soma, subtração, multiplicação e divisão) 
# usando apenas de estrutura de código orientada a objetos:


class Calculadora:
    def somar(self, n1, n2):
        return n1 + n2
    
    def subtrai(self, n1, n2):
        return n1 - n2
    
    def multiplica(self, n1, n2):
        return n1 * n2
    
    def divide(self, n1, n2):
        return n1 / n2
    

calc = Calculadora()

print(calc.somar(2,2))
print(calc.subtrai(10,2))
print(calc.multiplica(8,6))
print(calc.divide(124,12))