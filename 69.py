# Crie uma classe que armazena algumas características de um carro, em seguida crie dois carros distintos,
#  de características diferentes, usando da classe para construção de seus objetos/variáveis.

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def mostrar_modelo(self):
        print(f"O modelo do carro é: {self.modelo}")
    
    def mostrar_ano(self):
        print(f"O ano do carro é: {self.ano}")
    
    def mostrar_cor(self):
        print(f"A cor do carro é: {self.cor}")


c1 = Carro("Fusca", 2022, 'Preto')
c2 = Carro("Ferrari", 2025, 'Vermelho')

c1.mostrar_modelo()
c1.mostrar_ano()
c1.mostrar_cor()
print()
c2.mostrar_modelo()
c2.mostrar_ano()
c2.mostrar_cor()
