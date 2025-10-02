#variavel para armazenar o total de calorias
total_calorias = 0

#solicita ao usuario a quantidade de alimentos consumidos
quantidade_alimentos = int(input("Quantos alimentos você consumiu hoje? "))

#loop para repetir a solicitação de calorias para cada alimento
for x in range(1, quantidade_alimentos + 1):
    #para cada volta do loop, solicitar as calorias do alimento
    calorias_atuais = int(input("Informe as calorias do alimento {}: ".format(x)))
    #para cada caloria informada, somar ao total de calorias
    total_calorias = total_calorias + calorias_atuais

#exibicao do resultado!
print("\nO total de calorias consumidas no dia foi de: {} kcal.".format(total_calorias))

