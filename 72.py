# Crie uma classe Biblioteca que possui uma estrutura molde básica para cadastro de um livro de acordo com seu título,
#  porém que espera a inclusão de 
# um número não definido de títulos. Em seguida cadastre ao menos 5 livros nessa biblioteca:

class Biblioteca:
    def __init__(self, *args):
        self.livros = args


b = Biblioteca("Harry potter", "Narnia", "Crepusculo", "Clean code", "Matemática Legal")

print(b.livros)