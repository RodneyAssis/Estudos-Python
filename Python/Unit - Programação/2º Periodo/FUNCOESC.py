def Cadastro(Status_Aluguel, Nome_Placa, teste, relatorio, relatorio_Inativo):
    while True:
        cpf = input('\nDigite os 11 digitos do seu CPF ou 0 para sair: ')
        if cpf == '0':
            break
        while len(cpf) != 11 or cpf.isalpha():
            print('\nCPF invalido, Digite os 11 numeros do seu CPF')
            cpf = input('\nDigite os 11 digitos do seu CPF: ')
            if cpf == '0':
                break
        if cpf not in Status_Aluguel and len(cpf) == 11 and cpf.isnumeric():
            nome = input('Digite o nome do cliente: ').capitalize()
            placa = input('Digite a placa do carro: ')
            status = input('Ativo ou Inativo?: ').capitalize()
            while status not in ('Ativo', 'Inativo'):
                print('Digite somente Ativo ou Inativo')
                status = input('Ativo ou Inativo?: ').capitalize()
            if status == 'Ativo' or status == 'Inativo':
                Status_Aluguel[cpf] = status
                with open('Status_Aluguel.txt', 'a') as doc:
                    doc.write(str(cpf))
                    doc.write(str(' '))
                    doc.write(str(status))
                    doc.write(str('\n'))
                teste[cpf] = nome
                Nome_Placa[nome] = placa
                with open('nome_placa.txt', 'a') as doc:
                    doc.write(str(nome))
                    doc.write(str(' '))
                    doc.write(str(placa))
                    doc.write(str('\n'))
                if status == 'Ativo':
                        relatorio[nome] = placa
                        with open('relatorio_ativos.txt', 'a') as doc:
                            doc.write(str(nome))
                            doc.write(str(' '))
                            doc.write(str(placa))
                            doc.write(str('\n'))
                if status == 'Inativo':
                    relatorio_Inativo[nome] = placa
                    with open('relatorio_inativos.txt', 'a') as doc:
                        doc.write(str(nome))
                        doc.write(str(' '))
                        doc.write(str(placa))
                        doc.write(str('\n'))
                print('\nUsuário cadastrado com sucesso')
        else:
            print('\nO usuario ja esta cadastrado')


def Aluguel(Status_Aluguel, Aluguel_Vaga, Estacionamento, Nome_Placa, Relatorio):
    while True:
        print('Digite Sair em nome, para voltar ao menu')
        nome = input('\nDigite seu nome: ').capitalize()
        if nome == 'Sair':
            break
        cpf = input('\nDigite seu os 11 digitos do seu CPF: ')
        placa = input('\nDigite Placa do seu veiculo: ')
        if cpf in Status_Aluguel and Status_Aluguel.get(cpf) == 'Ativo' and placa in Nome_Placa.values()\
                and nome in Nome_Placa.keys():
            print('\nDigite a vaga do estacionamento que deseja')
            print('    0       1       2      3       4')
            for k in range(0, len(Estacionamento)):
                print(f'{k} {"  ".join(Estacionamento[k])}')
            linha = int(input('Digite a linha do estacionamento 0 a 3: '))
            coluna = int(input('Digite a coluna do Estacionamento 0 a 4: '))
            if linha and coluna == 'I 🚘 I':
                print('\nA vaga se encontra ocupada ')
            else:
                Aluguel_Vaga[cpf] = [linha, coluna]
                with open('Aluguel_Vaga.txt', 'a') as doc:
                    doc.write(str(cpf))
                    doc.write(str(' '))
                    doc.write(str(linha))
                    doc.write(' ')
                    doc.write(str(coluna))
                    doc.write(str('\n'))
                Estacionamento[linha][coluna] = 'I 🚘 I'
                Status_Aluguel[cpf] = 'Inativo'
                del Relatorio[nome]
                with open('Cliente_Vaga_alugada.txt', 'a') as texto:
                    texto.write(str(nome))
                    texto.write(str(' '))
                    texto.write(str(placa))
                    texto.write(str(' '))
                    texto.write(str(linha))
                    texto.write(str(' '))
                    texto.write(str(coluna))
                    texto.write(str('\n'))
                save_temp = list(Relatorio.keys())
                save_temp2 = list(Relatorio.values())
                with open('relatorio_ativos.txt', 'w') as doc:
                    for k in range(0, len(Relatorio)):
                        doc.write(f'{str(save_temp[k])} {str(save_temp2[k])}\n')
                save_temp3 = list(Status_Aluguel.keys())
                save_temp4 = list(Status_Aluguel.values())
                with open('Status_Aluguel.txt', 'w') as doc:
                    for k in range(0, len(Status_Aluguel)):
                        doc.write(f'{str(save_temp3[k])} {str(save_temp4[k])}\n')
                print('    0       1       2      3       4')
                for k in range(0, len(Estacionamento)):
                    print(f'{k} {"  ".join(Estacionamento[k])}')
        elif cpf in Status_Aluguel and Status_Aluguel.get(cpf) == 'Inativo':
            print('\nO usuário está inativo')
        else:
            print('\nUsuário não Cadastrado ou o número de placa está incorreto')
