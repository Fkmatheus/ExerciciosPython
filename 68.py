# Crie uma classe Pessoa, instancie a mesma por meio de uma variável e crie alguns atributos de classe 
# dando características a essa pessoa.
#  Por fim exiba em tela alguma mensagem que incorpore os atributos de classe criados:

class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def mostrar_nome(self):
        print(f"Olá! Meu nome é {self.nome}")
    
    def mostrar_altura(self):
        print(f"Olá! Minha altura é {self.altura}")
    
    def mostrar_idade(self):
        print(f"Olá! Minha idade é: {self.idade}")


p1 = Pessoa("Matheus", 25, 1.85)

p1.mostrar_nome()
p1.mostrar_idade()
p1.mostrar_altura()