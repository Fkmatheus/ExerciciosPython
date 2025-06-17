# Aprimore o exemplo anterior, incluindo um módulo simulando o cadastro de usuários em um plano de saúde, 
# apenas permitindo o agendamento de consulta caso o usuário que está interagindo com o programa conste no cadastro:

medicos = ["Gustavo", "Sthefany", "Leon"]

usuarios = {
    '01': "Carlos",
    '02': "Maria",
    '03': 'Enzo'
}

while True:
    user = input("Digite o seu usuário: ")

    if user not in usuarios.values():
        print("Usuário não cadastrado, tente novamente!")
        continue
    else:
        print(f"Bem vindo! {user}")
        break

q = 1
while q <= 3:
    print()
    print('     Médicos disponiveis:')
    print()
    for medico in medicos:
        print(medico)

    print()
    medico = input("Deseja consultar com qual médico? ")

    if medico not in medicos:
        print("Médico não está disponivel ou invalido.")
        print('Tente novamente...')
        q += 1
        continue

    else:
        print(f"Tudo certo! {user} sua consulta foi marcado com o Dr. {medico}")
        break