#criando um dicionário vazio
dicionario = {}
#exibindo o tipo do dicionário
print("O objeto dicionario é do tipo {}".format(type(dicionario)))

#criando um dicionário com dados
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
#exibindo o valor associado a uma chave específica
print(dicionario["R2-D2"])
#ou alternativamente
print(dicionario.get("R2-D2"))
#exibindo todos os valores em um dicionário
for valor in dicionario.values():
    print(valor)
#exibindo todas as chaves em um dicionário
for chave in dicionario.keys():
    print(chave)
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

#removendo o item cuja chave é R2-D2
dicionario.pop("R2-D2")
#removendo o último item
dicionario.popitem()
#removendo todos os itens do dicionário
dicionario.clear()
#exibindo o dicionário completo após a remoção
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))