
def verifica_maiores(n1, n2):
    if n1 > 100 and n2 > 100:
        print("Ambos os números são maiores que 100")
    elif n1 > 100:
        print(f'{n1} é maior que 100')
    else:
        print(f'{n2} é maior que 100')


verifica_maiores(102,101)