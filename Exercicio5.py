#faca um codigo que receba as 3 notas de um aluno e verifique se ele esta aprovado ou reprovado. considere que a media para aprovação é 7.0

#entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

##processamento
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Aluno aprovado\nMedia: {media:.2f}")
else:
    print(f"Aluno Reprovado\nMedia {media:.2f}")