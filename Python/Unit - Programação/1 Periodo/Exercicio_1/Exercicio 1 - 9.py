#9 - Faça um programa em Python para ler a idade de um nadador e imprimir a categoria onde o mesmo
#    se enquadra,conforme tabela abaixo:
#           • Infanil A: 5 - 7 anos;
#           • Infanil B : 8 - 10 anos;
#           • Juvenil A : 11 - 13 ano;
#           • Juvenil B : 14 - 17 anos;
#           • Adulto: maiores de 18 anos.

i = int(input("Digite sua idade: "))

if (i < 5):
    print("Categórias disponiveis somente apartir de 5 anos pra cima")
elif (i >= 5) and (i < 7):
    print("Você encontra-se na categória Infantil A")
elif (i >= 8) and (i < 10):
    print("Você encontra-se na categória Infantil B")
elif (i >= 11) and (i < 13):
    print("Você encontra-se na categória Juvenil A")
elif (i >= 14) and (i < 17):
    print("Você encontra-se na categória Juvenil B")
else:
    print("Você encontra-se na categória Adulto")