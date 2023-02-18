"""Utilizando as técnicas de código limpo, escreva um programa em
Python que realize o cadastro de questões objetivas para uma prova
com suas respectivas respostas.
Na sequência o programa deve solicitar as respostas para cada questão
e imprimir o resultado (acertos e erros). O programa deve permitir que
mais de uma pessoa informe as respostas, até que digite SAIR.
"""
import Funcao_Exercicio_1
Banco_Questoes = []
Gabarito_Alunos = []
try:
    Numero_Questoes = int(input("Digite o número de questões que deseja colocar: "))
    while Numero_Questoes <= 0 or Numero_Questoes > 200:
        print("\nPor favor, selecione somente números positivos entre 1 à 200.")
        Numero_Questoes = int(input("Digite o número de questões que deseja colocar: "))
    Banco_Questoes += Funcao_Exercicio_1.Definir_Respostas(Numero_Questoes)
except ValueError or OverflowError:
    print("Erro na digitação! Só pode ser selecionados numeros inteiros.")
print(Funcao_Exercicio_1.Quebra_pagina())

while True:
    Nome_Aluno = input("Digite o nome do aluno: ").title()
    Numero_Matricula = int(input("Digite o número de matricula: "))
    Gabarito_Alunos += Funcao_Exercicio_1.Resposta_Alunos(Nome_Aluno,
                                                          Numero_Matricula,
                                                          Banco_Questoes)
    Encerramento = input("Para encerrar, digite a palavra 'Sair'").capitalize()
    print(Funcao_Exercicio_1.Quebra_pagina())
    if Encerramento == 'Sair':
        break
print("\n\n")
print("-=-"*15, "Gabarito", "-=-"*15)
for i in range(len(Gabarito_Alunos)):
    print(Gabarito_Alunos[i])
