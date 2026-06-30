# Exercício de programação - Cálculo do IMC (Índice de Massa Corpórea) + Ellipsis

nome = "José Pedro"
peso = 73 
altura = 1.63
imc = peso / (altura ** 2) # IMC = peso / (altura * altura)
print("{} tem {} de altura, \n pesa {} kg e seu IMC é {:.2f}".format(nome, altura, peso, imc))