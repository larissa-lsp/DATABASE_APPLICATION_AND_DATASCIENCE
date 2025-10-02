#Criando a função de saudação
def fSaudacao(pPeriodo, *pNome): # * para passar vários nomes
 for i in pNome:
    if pPeriodo.lower() in ('manha', 'm'):
      print(f'Bom dia, {i}! Como vai?')
    elif pPeriodo.lower() in ('tarde', 't'):
      print(f'Boa tarde, {i}! Como vai?')
    else:
      print(f'Boa noite, {i}! Como vai?')
# #aqui começa o programa principal
fSaudacao('n', 'João', 'Maria', 'Pedrinho')