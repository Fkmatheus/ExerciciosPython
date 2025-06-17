# Crie um programa modularizado, onde em um arquivo teremos uma lista de médicos fictícios a serem consultados, 
# em outro arquivo, teremos a estrutura principal do programa, 
# que por sua vez realiza o agendamento de uma consulta médica com base na interação com o usuário.

medicos = ["Matheus", "Gustavo", "Sthefany"]

medico = input("Digite com qual médico você deseja consultar: ")

if medico not in medicos:
    print("Não existe esse médico nesse hospital")
else:
    print(f"Consulta marcada com {medico}")