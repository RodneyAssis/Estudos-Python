#  2 - Faça um programa usando Python para ler a nota da primeira unidade de um aluno de Fundamentos de Programação.
#      Calcule e imprima o valor mínimo que este aluno precisará obter na segunda unidade para ser aprovado.

Nota = float(input("Digite a nota da sua 1º Unidade:"))

Nota2 = (6*2) - Nota

if Nota <= 4:
    print("Reprovado")

else:
    print("Você precisa tirar {} para passar na média.".format(Nota2))