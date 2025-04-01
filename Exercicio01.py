#faça um programa para ler o nome de uma pessoa, a sua idade e o salario e mostre essas informações

#entrada de dados
nome = input("Insira o seu nome: ")
idade = int(input("Insira a sua idade: "))
salario = float(input("Informe o seu salario: "))
aumentoSalario = float(input("Infome a porcentagem do salario: "))

#processamento
aumento = (salario*aumentoSalario)/100
novoSalario = salario+aumento

#saida de dados
print(f"Olá {nome}, você tem {idade} anos de vida. O seu salário era de R${salario:.2f} mensais.\nObteve um aumento de R${aumento:.2f}\nSeu novo salario é de R${novoSalario:.2f} ")