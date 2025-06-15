# Crie uma simples estrutura de dados simulando um cadastro para uma loja.
#  Nesse cadastro deve conter informações como nome, 
# idade, sexo, estado civil, nacionalidade, faixa de renda, etc... Exiba em tela tais dados:

dados = {
    'Nome': "",
    'Sexo': "",
    'CV': "",
    'nacionalidade': "",
    'faixaderenda': ""
}

def exibe_dados(dados):
    print(f""" 
    Nome: {dados['nome']}
    Sexo: {dados['sexo']}
    CV: {dados['CV']}
    Nacionalidade: {dados['nacionalidade']}
    Faixa de Renda: {dados['faixaderenda']}

""")
    
dados['nome'] = input("Digite seu nome: ")
dados['sexo'] = input("Digite o seu sexo: ")
dados['CV'] = input("Digite o seu estado civil: ")
dados['nacionalidade'] = input("Digite a sua nacionalidade: ")
dados['faixaderenda'] = input("Digite a sua faixa de renda: ")

print()
exibe_dados(dados)




    
