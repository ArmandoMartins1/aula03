#ler 2 numeros, efetuar as 4 operações matematicas e mostrar os resultados
#entrada de dados
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o primeiro numero: "))

#processamento
soma= n1+n2             #soma
subtracao= n1-n2        #subtração
multiplicacao = n1*n2   #multiplicacao
divisao = n1/n2         #divisao

#saida
print(f"Soma: {soma}\nSubtração: {subtracao}\nMultiplicação: {multiplicacao:.2f}\nDivisão: {divisao:.2f}")