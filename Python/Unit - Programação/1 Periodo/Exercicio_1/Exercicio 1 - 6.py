#6 - Faça um programa usando Python para ler as duas notas de um aluno de Fundamentos de Programação.
#    Calcule e imprima a sua média, de acordo com os critérios da UNIT e uma mensagem conforme a situação abaixo:
#    Média           Mensagem
#  Menor que 4       Reprovado
#  Entre 4 e 6      Recuperação
#Maior ou igual a 6  Aprovado

Nota1 = float(input("Digite a nota da primeira unidade: "))
Nota2 = float(input("Digite a nota da primeira unidade: "))

media = (Nota1 +Nota2)/2

if Nota1 <= 4:
    print("\nReprovado")
    print("Pois você tirou {} na 1º Unidade".format(Nota1))


elif (media <= 5.9) and (media > 4):
    print("\nVocê está de Recuperação")
    print("({}+{})/2 = {}".format(Nota1,Nota2,media))

elif media >= 6:
    print("\nVocê está Aprovado")
    print("({}+{})/2 = {}".format(Nota1,Nota2,media))