# A partir de um simples dicionário composto por três itens, {‘Alto Nível’: ‘Python, ‘Médio Nível’: 
# ’C’, ‘Baixo Nível’: 
# ‘Assembly’}, 
# verifique se ‘Python’ consta no dicionário em questão, utilizando de negação lógica para tal verificação:

dicio = {'Alto Nível': 'Python',
         'Médio Nível': 'C',
         'Baixo Nível': 'Assembly'}

if 'Python' in dicio.values():
    print("Python está presente")
else:
    print("Python não está presente")