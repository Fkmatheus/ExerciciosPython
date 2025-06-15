# Crie um sistema de perguntas e respostas que interage com o usuário, 
# pedindo que o mesmo insira uma resposta. Caso a primeira questão esteja correta, 
# exiba em tela uma mensagem de acerto e parta para a próxima pergunta, 
# caso incorreta, exiba uma mensagem de erro peça para tentar novamente:


print("Quanto é 1 + 1 ?")
while True:
    resposta1 = input("Qual é a resposta da primeira pergunta? ")
    if resposta1 != '2':
        print("Resposta errada... Tente novamente")
        continue
    
    break

print("Quanto é 2 + 2 ?")

while True:
    resposta2 = input("Qual é a resposta da segunda pergunta? ")
    if resposta2 != '4':
        print("Resposta errada... Tente novamente")
        continue
    
    break

print("Parabéns você venceu!")