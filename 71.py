# Crie uma classe de nome Inventario com os atributos de classe pré-definidos item1 e item2, 
# a serem cadastrados manualmente pelo usuário, simulando um simples carrinho de compras:

class Inventario:
    def __init__(self, item1, item2):
        self.item1 = item1
        self.item2 = item2


item1 = input("Digite o primeiro item: ")
item2 = input("Digite o segundo item: ")

inv = Inventario(item1, item2)

print(inv.item1, inv.item2)