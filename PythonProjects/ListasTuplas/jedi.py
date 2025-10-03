#criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
#criação dos elementos acima, respectivamente: 0, 1, 2, 3. Como também assume: -4, -3, -2, -1
#exibindo um valor específico da lista a partir do último
print(jedi[-1])

#incluindo um valor no final da lista
jedi.append("Mace Windu")

#incluindo um valor em uma posição específica da lista
jedi.insert(2, "Luminara")

#A variável assumirá cada um dos valores da lista
for nome in jedi:
    #para cada volta do loop, exibir o valor assumido
    print(nome)

#incluindo um valor pelo usuário em uma posição específica da lista
#jedi.insert(2, input("Digite o nome de um Jedi "))

#Removendo o último valor inserido na lista
jedi.pop()
print(jedi)

#Removendo um valor em uma posição específica
jedi.pop(2)
print(jedi)

#criação de uma lista com os nomes dos Jedi
outros_jedis = ["Mace Windu", "Qui-Gon Jinn", "Kit Fisto"]
jedis_completos = jedi + outros_jedis
print(jedis_completos)

jedi_copia = jedi.copy()
jedi_copia.append("Rey")
print(jedi_copia) # ['Yoda', 'Luke', 'Obi-Wan', 'Anakin', 'Rey']

primeiros_jedis = jedi[:3] # acessa os 3 primeiros jedis.csv
ultimos_jedis = jedi[-3:] # acessa os 3 últimos jedis.csv
jedis_pares = jedi[::2] # acessa os jedis.csv em índices pares
print(primeiros_jedis) # ['Yoda', 'Luke', 'Obi-Wan']
print(ultimos_jedis) # ['Mace Windu', 'Qui-Gon Jinn', 'Kit Fisto']
print(jedis_pares) # ['Yoda', 'Obi-Wan', 'Mace Windu', 'Kit Fisto']

jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin", "Mace Windu", "Qui-Gon Jinn", "Kit Fisto"]
# Inverte a palavra "Anakin" usando slicing
anakin_invertido = jedi[3][::-1]
# Imprime a palavra invertida
print(anakin_invertido) # "nikanA"