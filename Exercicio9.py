"""receba, do usuario, um numero de 1 a 12 e mostre o nome do mês correspondente.
caso o mês não exista, mostrar: "Valor inválido".
obs: usando if/elif/else"""
#entrada de dados
num = int(input("Digite um numero entre 1 e 12: "))

#processamento
if (num <1) or (num>12):
    print("valor invalido!")
else:
    if num == 1:
        print("Janeiro")
    elif num == 2:
        print("Fevereiro")
    elif num == 3:
        print("Março")
    elif num == 4:
        print("Abril")
    elif num == 5:
        print("Maio")
    elif num == 6:
        print("Junho")
    elif num == 7:
        print("Julho")
    elif num == 8:
        print("Agosto")
    elif num == 9:
        print("Setembro")
    elif num == 10:
        print("Outubro")
    elif num == 11:
        print("Novembro")
    elif num == 12:
        print("Dezembro")