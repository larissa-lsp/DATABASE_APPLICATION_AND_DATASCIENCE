#criando um dicionário vazio
dicionario = {}
#incluindo dados no dicionário
dicionario["André David"] = "Professor"
#alterando dados no dicionário
dicionario["André David"] = "Coordenador"
print(dicionario)
#substituindo o cargo de coordenador por supervisor
dicionario.update({"André David":"Supervisor"})
print(dicionario)
#parece substituir mas acrescenta
dicionario.update({"Patrícia Angelini":"Diretora"})
print(dicionario)