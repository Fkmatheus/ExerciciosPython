# Crie uma função que pode conter dois ou mais parâmetros, porém sem um número definido e declarado de parâmetros:

def recebe_valores(*args):
    print(args)

recebe_valores(1,2,3,4)