# Crie uma função que recebe parâmetros tanto por justaposição quanto nomeados a partir de 
# uma lista e de um dicionário,
#  desempacotando os elementos e reorganizando os mesmos como parâmetros da função:

def show_data(*args, **kwargs):
    print(args)
    print(kwargs)




numeros = [1,2,3,4,5]

dados = {'Nome': "Matheus", "Tel": '999999999'}



show_data(*numeros, **dados)