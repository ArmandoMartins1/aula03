#escreva um algoritmo que leia o numero de litros vendidos e o tipo de combustivel (codificado da seguinte forma: E-etanol, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo que o preço do litro da gasolina é R$5.80 e o etanol R$4.90
#entrada
print(" // ")
tipoCombustivel = input("Qual foi o tipo do combustivel:\n"
                        "G - Gasolina\n"
                        "E - Etanol\n"
                        "Tipo do combustivel? ")
combustivel = float(input("Quantidade de litros: "))
gasolina = 5.8
etanol = 4.9
##processamento
'''
if tipoCombustivel == "G":
    print(f"O valor a ser pago é R${combustivel * gasolina:.2f}")
else:
    if tipoCombustivel == "g":
        print(f"O valor a ser pago é R${combustivel * gasolina:.2f}")
    else:
        if tipoCombustivel == "e":
            print(f"O valor a ser pago é R${combustivel * etanol:.2f}")
        else:
            if tipoCombustivel == "E":
                print(f"O valor a ser pago é R${combustivel * etanol:.2f}")
            else:
                print("Tipo do combustivel não identificado!")
'''
'''
if tipoCombustivel == "G":
    valor = combustivel * gasolina
else:
    if tipoCombustivel == "g":
        valor = combustivel * gasolina
    else:
        if tipoCombustivel == "E":
            valor = combustivel * etanol
        else:
            if tipoCombustivel == "e":
                valor = combustivel * etanol
            else:
                print("Tipo incorreto!")
'''

if tipoCombustivel == "G" or tipoCombustivel == "g":
    valor = combustivel*gasolina
elif tipoCombustivel == "e" or tipoCombustivel == "E":
    valor = combustivel*etanol
else:
    print("Tipo incorreto!")

print(f"O valor a ser pago é R${valor:.2f}")