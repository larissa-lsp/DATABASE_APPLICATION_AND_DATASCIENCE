try: #TRY coloca-se tudo o que se espera que funcione corretamente, ou seja, o fluxo do programa
   idade = int(input("Por favor, insira a idade do aluno: "))
except ValueError: #EXCEPT para tratamento de exceções
   print("Você não inseriu uma idade válida. Por favor, insira um número inteiro.")
else:
   print("A idade do aluno é:", idade)
finally: #FINALLY execute independente se houver exceções e o fluxo normal
    print("Obrigado por usar nosso programa!")

try:
    number = int(input("Insira um número: "))
    if number < 0:
        raise ValueError("Número não pode ser negativo")
except ValueError as error:
    print("Erro:", error)
    raise #RAISE permite que você processe uma exceção e, em seguida, a lance novamente para ser tratada em outro lugar no código