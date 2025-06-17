# Crie uma função que recebe parâmetros tanto por justaposição (*args) quanto nomeados (**kwargs):

def argumentos(*args, **kwargs):
    for k in args:
        print(k,sep=" ")
    
    for key, item in kwargs.items():
        print(key, item)





argumentos(1,2,3,nome="Matheus",sexo="M")