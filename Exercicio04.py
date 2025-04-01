#Receba 2 números do usuario e mostre eles em ordem crescente
#entrada
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

#processamento e saida
if n1>n2:
    print(f"{n2} {n1}")
else:
    print(f"{n1} {n2}")