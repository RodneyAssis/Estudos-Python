def carregar_cliente(cliente_c):
    with open('Status_Aluguel.txt') as doc:
        for line in doc:
            (cpf, name) = line.split()
            cliente_c[cpf] = name


def carregar_nome_placa(cliente_c):
    with open('nome_placa.txt') as doc:
        for line in doc:
            (nome, placa) = line.split()
            cliente_c[nome] = placa


def carregar_Aluguel_Vaga(reserva):
    with open('Aluguel_Vaga.txt') as doc:
        for line in doc:
            (cpf, name, name2) = line.split()
            reserva[cpf] = [int(name), int(name2)]


def carregar_vagas(estacionamento, reserva):
    contador = 0
    contador2 = 0
    teste = []
    teste += reserva.values()
    while True:
        estacionamento[teste[contador2][0]][teste[contador2][1]] = 'I 🚘 I'
        contador2 += 1
        contador += 1
        if contador == len(teste):
            break


def carregar_relatorio_ativos(cliente_c):
    with open('relatorio_ativos.txt') as doc:
        for line in doc:
            (nome, placa) = line.split()
            cliente_c[nome] = placa


def relatorio_inativos(cliente_c):
    with open('relatorio_inativos.txt') as doc:
        for line in doc:
            (nome, placa) = line.split()
            cliente_c[nome] = placa