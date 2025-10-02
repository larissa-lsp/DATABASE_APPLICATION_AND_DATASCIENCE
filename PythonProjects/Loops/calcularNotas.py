# Variaveis para armazenar a soma das notas dos alunos impares e pares
soma_notas_impares = 0.0
soma_notas_pares = 0.0

# Loop para solicitar as notas dos 25 alunos com número ímpar
# O range(1, 50, 2) cria uma sequência de 1 a 49, pulando de 2 em 2
print("INSERIR NOTAS DOS ALUNOS ÍMPARES")

for x in range(1,50,2):
    print("\nVocê está digitando as notas dos alunos ímpares.")
    nota_impar = float(input(f"Insira a nota do aluno de número  {x}: "))
    soma_notas_impares = soma_notas_impares + nota_impar

print("INSERIR NOTAS DOS ALUNOS PARES")

# Loop para solicitar as notas dos 25 alunos com número par
for x in range(2,51,2):
    print("\nVocê está digitando as notas dos alunos pares.")
    nota_par = float(input(f"Insira a nota do aluno  {x}: "))
    soma_notas_pares = soma_notas_pares + nota_par

media_notas_impares = soma_notas_impares / 25
media_notas_pares = soma_notas_pares / 25

print(f"\nA média de notas da metade ímpar da sala foi: {media_notas_impares}")
print(f"\nA média de notas da metade par da sala foi: {media_notas_impares}")
