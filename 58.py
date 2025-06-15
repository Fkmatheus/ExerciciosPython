# Crie uma função com dois parâmetros, sendo um deles com um dado/valor predeterminado:

def potencia(n,eleva=2):
    return n ** eleva

resultado1 = potencia(2)
resultado2 = potencia(2,4)
resultado3 = potencia(5,10)

print(resultado1, resultado2, resultado3)