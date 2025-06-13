# Crie um programa que exibe em tela a tabuada de um determinado número fornecido pelo usuário:

n = int(input("Digite um número: "))

def tabuada(n):
    print(f""" 
    {n} X 1: {n*1}
    {n} X 2: {n*2}
    {n} X 3: {n*3}
    {n} X 4: {n*4}
    {n} X 5: {n*5}
    {n} X 6: {n*6}
    {n} X 7: {n*7}
    {n} X 8: {n*8}
    {n} X 9: {n*9}
    {n} X 10: {n*10}

""")
    
tabuada(n)