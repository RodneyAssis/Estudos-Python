import FUNCOES
import FUNCOESC
import CARREGAMENTOS

Estacionamento = FUNCOES.Estacionamento()
Aluguel_Vaga = {}
Status_Aluguel = {}
Nome_Placa = {}
Relatorio = {}
Relatorio_inativos = {}
teste = {}

try:
    CARREGAMENTOS.carregar_relatorio_ativos(Relatorio)
except FileNotFoundError:
    open("relatorio_ativos.txt", "w")
try:
    CARREGAMENTOS.carregar_Aluguel_Vaga(Aluguel_Vaga)
except FileNotFoundError:
    open('Aluguel_Vaga.txt', 'w')
try:
    CARREGAMENTOS.carregar_cliente(Status_Aluguel)
except FileNotFoundError:
    open("Status_Aluguel.txt", "w")
try:
    CARREGAMENTOS.carregar_nome_placa(Nome_Placa)
except FileNotFoundError:
    open("nome_placa.txt", "w")
try:
    CARREGAMENTOS.carregar_vagas(Estacionamento, Aluguel_Vaga)
except IndexError:
    print()
try:
    CARREGAMENTOS.relatorio_inativos(Relatorio_inativos)
except FileNotFoundError:
    open("relatorio_inativos.txt", "w")

print('     \033[0;33mI 🚘 I   Bem vindo ao estacionamento express  I 🚘 I\n'
      'I 🚧 I   Na Car Express damos total suporte ao seu veiculo I 🚧 I\n'
      '                   Em breve novidades\033[0;00m')
FUNCOES.estacionamento(Estacionamento)
while True:
    menu = input('\n\033[0;32m1 - Cadastro de clientes '
                 '\n2 - Alugar vaga'
                 '\n3 - Relatório de clientes que reservaram vagas'
                 '\n4 - Relatório de clientes Ativos'
                 '\n5 - Relatório de clientes Inativos'
                 '\n0 - Desligar console\n'
                 '\n\033[1;36mDigite um número do menu:\033[0;00m ')

    if menu not in ('0', '1', '2', '3', '4', '5'):
        print('\nDigite Somente números do Menu')
    if menu == '0':
        print('\n\nObrigado por escolher a express.\n'
              'Car Express, tudo para o seu veiculo em um só lugar ')
        FUNCOES.carro()
        break
    if menu == '1':
        FUNCOESC.Cadastro(Status_Aluguel, Nome_Placa, teste, Relatorio, Relatorio_inativos)
    if menu == '2':
        FUNCOESC.Aluguel(Status_Aluguel, Aluguel_Vaga, Estacionamento, Nome_Placa, Relatorio)
    if menu == '3':
        FUNCOES.relatorio_vagas_alugadas()
    if menu == '4':
        FUNCOES.relatorio_ativos()
    if menu == '5':
        FUNCOES.relatorio_inativos()
