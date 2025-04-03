#receba um numero e diga se ele é par ou impar
#entrada de dados
numero = int(input("Digite um valor inteiro: "))

#processamento
if numero % 2 == 0:
    print(f"{numero} é PAR")
else:
    print(f"{numero} é IMPAR")