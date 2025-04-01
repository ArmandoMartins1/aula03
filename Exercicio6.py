#Ler o nome de 2 times e o numero de gols marcados na partida(para cada time). Escrever o nome do vencedor. caso não haja vencedor deverá ser impressa a palavra EMPATE
#entrada de dados
time1 = input("Primeiro time: ")
golTime1 = int(input(f"Quantos gols o {time1} fez? "))
time2 = input("Segundo time: ")
golTime2 = int(input(f"Quantos gols o {time2} fez? "))

if golTime1>golTime2:
    print(f"O {time1} venceu com o placar de {golTime1}x{golTime2}")
else:
    if golTime2>golTime1:
        print(f"O {time2} venceu com o placar de {golTime2}x{golTime1}")
    else:
        print(f"EMPATE\n"
              f"Com o placar de {golTime1}x{golTime2}")

