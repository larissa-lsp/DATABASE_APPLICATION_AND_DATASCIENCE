#usando a função open para criar um objeto do tipo arquivo
arquivo = open("E:\aulas_programacao\Projetos\MeuPrimeiroProjeto\arquivo_de_texto.txt")

#printando uma linha do arquivo
print(arquivo.readline())

#printando outra linha do arquivo
print(arquivo.readline())

#descobrindo onde está o controle do arquivo
print("Atualmente o arquivo está em:", arquivo.tell())

#voltando para a primeira linha
arquivo.seek(0)
print("Agora o arquivo está em:", arquivo.tell())
#printando a primeira linha do arquivo
print(arquivo.readline())
arquivo.close()
#Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#Escrevendo o conteúdo da variável conteudo dentro do arquivo
#arquivo.write(conteudo)



