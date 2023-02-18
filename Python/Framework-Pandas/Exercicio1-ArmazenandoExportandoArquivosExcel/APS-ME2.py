import pandas as pd

# Importando os arquivos do Excel para o Python

# Arquivos alunos
dados_aluno = {'Nome': [], 'Matricula': [], 'Data de Nasc.': []}
try:
    Excel_Aluno = pd.read_excel("UNIGRANDE.xlsx", sheet_name='Alunos')
    Exporta = Excel_Aluno.to_dict('list')
    dados_aluno['Nome'], dados_aluno['Matricula'] = Exporta['Nome'], Exporta['Matricula'],
    dados_aluno['Data de Nasc.'] = Exporta['Data de Nasc.']
except FileNotFoundError:
    pass

print(dados_aluno)

# Arquivos professores
dados_prof = {'Nome': [], 'Matricula': [], 'Data de Nasc.': []}
try:
    Excel_Professor = pd.read_excel("UNIGRANDE.xlsx", sheet_name='Professores')
    Exporta = Excel_Professor.to_dict('list')
    dados_prof['Nome'], dados_prof['Matricula'] = Exporta['Nome'], Exporta['Matricula'],
    dados_prof['Data de Nasc.'] = Exporta['Data de Nasc.']
except FileNotFoundError:
    pass

while True:
    opcao = int(input("1- Cadastro do professor\n"
                      "2- Cadastro do Aluno\n"
                      "3- Cadastro da Disciplina\n"
                      "4- Cadastro de notas\n"
                      "5- Relatorio de Notas\n"
                      "6- Sair do Sistema\n\n"
                      "Escolha uma das alternativas: "))

    # Cadastro dos Professores
    if opcao == 1:
        P_Matricula = input("Matricula do professor: ")
        P_Nome = input("Nome do professor:")
        P_Nascimento = input("Data de nascimento do professor: ")

        dados_prof['Nome'] += [P_Nome]
        dados_prof['Matricula'] += [P_Matricula]
        dados_prof['Data de Nasc.'] += [P_Nascimento]

        dataframe_professor = pd.DataFrame(dados_prof)
        dataframe_professor.to_excel('UNIGRANDE.xlsx', sheet_name='Professores', index=False)

    # Cadastro dos Alunos
    if opcao == 2:
        A_Matricula = input("Matricula do aluno: ")
        A_Nome = input("Nome do aluno: ")
        A_Nascimento = input("Data de nascimento do aluno: ")

        dados_aluno['Nome'] += [A_Nome]
        dados_aluno['Matricula'] += [A_Matricula]
        dados_aluno['Data de Nasc.'] += [A_Nascimento]

        dataframe_alunos = pd.DataFrame(dados_aluno)
        dataframe_alunos.to_excel('UNIGRANDE.xlsx', sheet_name='Alunos', index=False)

    # Cadastro de Disciplinas
    if opcao == 3:
        D_Codigo = input("Código da disciplina: ")
        D_Nome = input("Nome da Disciplina")
        D_MatProfessor = input("Matricula do professor")

    # Sair do Sistema
    if opcao == 6:
        break
