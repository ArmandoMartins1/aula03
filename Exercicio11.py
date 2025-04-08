#escreva um algoritmo para ler 10 numeros e ao final da leitura escrever a soma total dos 10 numeros lidos.
somaNum = 0
for i in range(1,11,1):
    num = int(input(f"Digite o {i} numero: "))
    somaNum =somaNum + num
print(somaNum)
