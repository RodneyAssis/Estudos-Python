def Definir_Respostas(Numero_Questoes):
    Banco_Questoes = []
    print("Opções de alternativas: A, B, C, D, E")
    for Questoes in range(1, Numero_Questoes + 1):
        Resposta = input(f"Digite a Resposta de {Questoes}º Questão: ").lower()
        while Resposta not in ['a', 'b', 'c', 'd', 'e']:
            print("Por favor, selecione somente as alterantivas acima.")
            Resposta = input(f"Digite a Resposta de {Questoes}º Questão: ").lower()
        Banco_Questoes.append(Resposta)
    return Banco_Questoes


def Resposta_Alunos(Nome_Aluno, Numero_Matricula, Banco_Questoes):
    Gabarito_Alunos = []
    Num_Questoes_Respondidas = 0
    Corretas = 0
    Incorretas = 0
    print("Opções de alternativas: A, B, C, D, E")
    while Num_Questoes_Respondidas != len(Banco_Questoes):
        Resposta_Aluno = input(f"Digite a Resposta de {Num_Questoes_Respondidas + 1}ºQuestão: ").lower()
        while Resposta_Aluno not in ['a', 'b', 'c', 'd', 'e']:
            print("Por favor, selecione somente as alterantivas acima.")
            Resposta_Aluno = input(f"Digite a Resposta de {Num_Questoes_Respondidas + 1}ºQuestão").lower()
        if Resposta_Aluno == Banco_Questoes[Num_Questoes_Respondidas]:
            Corretas += 1
        else:
            Incorretas += 1
        Num_Questoes_Respondidas += 1
    Gabarito_Alunos += [f"Aluno: {Nome_Aluno} | "
                        f"Matricula: {Numero_Matricula} | "
                        f"Acertos: {Corretas} | "
                        f"Erros: {Incorretas} | "
                        f"Porcentagem de acertos: {(Corretas/len(Banco_Questoes))*100}%"]
    return Gabarito_Alunos


def Quebra_pagina():
    return "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
