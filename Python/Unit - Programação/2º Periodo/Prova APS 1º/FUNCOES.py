def Estacionamento():
    vagas = []
    for x in range(4):
        linhas = []
        for i in range(5):
            linhas.append('I 🚧 I')
        vagas.append(linhas)
    return vagas


def Cancelamentos():
    while True:
        consulta = input('\nDeseja consultar o relatório de cancelamentos? [S/N] ').upper()
        if consulta == 'S':
            print('\n\033[0;31mCancelamentos registrados de acordo com CPF\033[0;00m\n')
            try:
                with open('relatorio_cancel.txt', 'r') as canc:
                    for linha in canc:
                        linha = linha.strip()
                        print(linha)
            except FileNotFoundError:
                open('relatorio_cancel.txt', 'w')
        else:
            break


def relatorio_ativos():
    while True:
        consulta = input('\nDeseja consultar o relatorio de cliente ativos? [S/N] ').upper()
        if consulta == 'S':
            print('\n\033[0;32mRelatorio de clientes ativos F\033[0;00m\n')
            print('NOME    PLACA')
            try:
                with open('relatorio_ativos.txt', 'r') as canc:
                    for linha in canc:
                        linha = linha.strip()
                        print(linha)
            except FileNotFoundError:
                open('relatorio_ativos.txt', 'w')
        op = input('\nDeseja sair? ').upper()
        if op == 'S':
            break


def relatorio_inativos():
    while True:
        consulta = input('\nDeseja consultar o relatorio de cliente invativos? [S/N] ').upper()
        if consulta == 'S':
            print('\n\033[0;32mRelatorio de clientes inativos \033[0;00m\n')
            print('NOME    PLACA')
            try:
                with open('relatorio_inativos.txt', 'r') as canc:
                    for linha in canc:
                        linha = linha.strip()
                        print(linha)
            except FileNotFoundError:
                open('relatorio_ativos.txt', 'w')
        op = input('\nDeseja sair? ').upper()
        if op == 'S':
            break


def relatorio_vagas_alugadas():
    while True:
        consulta = input('\nDeseja consultar o relatorio de clientes que possuem vagas alugas? [S/N] ').upper()
        if consulta == 'S':
            print('\n\033[0;32mRelatorio de clientes com vagas alugadas'
                  '\nNome placa e vaga alugada\033[0;00m\n')
            try:
                with open('Cliente_Vaga_alugada.txt', 'r') as canc:
                    for linha in canc:
                        linha = linha.strip()
                        print(linha)
            except FileNotFoundError:
                open('Cliente_Vaga_alugada.txt', 'w')
        op = input('\nDeseja sair? ').upper()
        if op == 'S':
            break


def estacionamento(Estacionamento):
    print('    0       1       2      3       4')
    for k in range(0, len(Estacionamento)):
        print(f'{k} {"  ".join(Estacionamento[k])}')


def carro():
    print('⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄'
          '\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄'
          '\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄'
          '\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄'
          '\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄'
          '\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\033[0;33m⢀⣀⣠⣤⣤⣤⣤⣤⣤⣀⣀⣀⣀\033[0;00m⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄'
          '\033[0;33m⢠⢀⠄⢤⡤⠚⠋⢡⡀\033[0;00m'
          '\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\033[0;33m⣀⣀⠤⠤⠒⣚⣛⡩⠤⠤⠤⠤⠤⠤⠤⢤⢄⣀⣀⣀⣀⠈⠉⠉⠛⠛⠒⠒⠢⠤⠤⠤⢄⣀⣀⣀⠄⡴⢁⠋⠘⡀'
          '⠤⠤⠐⠚⠃\033[0;00m'
          '\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\033[0;33m⢀⣀⡠⠶⠒⣉⣉⠤⠶⣒⠉⠉⠁\033[0;00m⠄⠄⠄⠄⠄⠄⠄⠄\033[0;33m⠈⢏⣎⣄⣉⠹⠭⡿⣒⠒⠲⢦\033[0;00m'
          '⠄⠄⠄⠄⠄⠄⠄\033[0;33m⠉⠉⠉⠉⠛⠒⠶⠶⣦⣤\033[0;00m⠄⠄⠄'
          '\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\033[0;33m⣀⣤⠤⠒⠒⠈⠉⠉⠉⠑⠒⠚⢭⣤⣢⡭⣡⣀⣀⣠⣤⣤⠤⠤⠔⠒⠒⠒⠒⠉⠉⠛⢤⡀⠄⣂⡼⠄⠊⠁⣠\033[0;00m⠄⠄⠄⠄⠄⠄⠄⠄⠄'
          '⠄\033[0;33m⠤⠐⢲⡯⢳⡆⠄⠄⠄'
          '\n⠄⠄⠄⠄⠄⢀⣤⢔⠛⠉⠄⢀⡤⡲⠏⢉⠉⠽⣖⢤⡀⠄⣼⠄⠄⠉⠘⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡴⠶⠄⣾⣤⠤⣤⠄⠄⢀⠆⠄⢠⢔⡯⠕⣒⠊⠭⣒⢤⠄⠄⠈⠉⠁⠸⠄⠄⠄'
          '\n⠄⢀⡠⠖⡺⢂⠹⠉⠄⠄⣰⡹⣩⠎⠙⡇⠸⠋⠲⡕⠞⢆⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⠁⠄⢠⠃⠄⠄⠄⠄⣜⣝⡱⠊⠱⡆⡖⠉⠦⡱⡙⡀⠄⠄⢠⡇⠄⠄⠄'
          '\n⠄⢪⢀⣈⡉⠉⠄⠄⠄⠄⢧⢁⠛⠤⢤⠗⢶⡠⠴⢾⣼⣼⢹⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡴⠁⠄⣀⠏⠄⠄⠄⠄⢸⠙⢸⠳⠤⢴⠗⢧⠤⠶⢳⢻⢷⠄⠄⣸⡁⠄⠄⠄'
          '\n⢀⣼⡆⠈⠑⢦⠄⠄⠄⢸⡘⡌⡶⠂⠘⡂⠞⠉⠐⣺⢹⢻⠸⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⠚⠁⣠⠖⠉⠄⠄⠄⠄⠄⢸⢰⢸⡖⠊⠙⡖⡟⠁⠒⡼⡾⣾⡤⠒⠉⡝⠄⠄⠄'
          '\n⠘⠣⢽⣟⡲⠾⢤⢤⢤⢼⣧⣿⣌⢦⣤⠃⢸⣤⡜⣳⣧⣏⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣒⣒⣒⣒⣒⣒⣒⣒⣚⣛⣀⣀⣀⣀⣀⣀⣀⣀⣸⣎⣣⡕⢤⣼⡃⢳⣤⢚⣼⣀⣇⣀⣀⣰⡇⠄⠄⠄'
          '\n⠄\033[0;00m⢀⠄⡀⢀\033[0;33m⠈⠉⠉⠉⠉\033[0;00m⢀⠄⢀\033[0;33m⠑⠒⠺⠖⠒⠉\033[0;00m⠄\033[0;00m'
          '⢀⠄⢀⠄⡀⢀⠄⡀⢀⠄⡀⢀⠄⡀⢀⠄⡀⢀⠄⡀⢀⠄⡀⢀⠄⡀⢀⠄⡀⢀⠄⢀⠄'
          '\033[0;33m⠈⠑⠒⠒⠒⢈⠁\033[0;00m⢀⠄⡀⢀⠄⡀⠄⠄⠂⠄')