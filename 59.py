# Crie uma função com três parâmetros, sendo dois deles com dados/valores padrão, 
# alterando o terceiro deles contornando o paradigma da justaposição de argumentos:

def cadastro(nome, tel=1111111,cidade='Porto Alegre'):
    print(f""" 
    Tel: {tel}
    Cidade: {cidade}
    Nome: {nome}
""")
    

cadastro("Matheus", cidade="São Paulo")