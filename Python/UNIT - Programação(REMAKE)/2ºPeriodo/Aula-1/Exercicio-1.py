"""Você está iniciando um novo negócio: uma locadora de veículos. Para iniciar o
controle do aluguel de carros é necessário um sistema simples. Dessa forma,
desenvolva um programa um Python para:
a) Solicitar ao usuário informações sobre as locações: nome do cliente, sexo (F- Feminino, M -
Masculino), placa do carro alugado, quantidade de quilômetros contratados, quantidade de dias
contratados;
b) Calcular e imprimir a placa do carro e valor total a pagar para CADA cliente, considerando que
deverá ser cobrado o valor de R$ 70,00 por dia contratado, e R$ 0,10 para cada quilômetro
contratado;
c) Calcular e imprimir a média de quilômetros contratados pelos clientes;
d) Calcular e imprimir o nome das clientes de sexo feminino que fecharam aluguéis acima de 7 dias
contratados.
Obs.: o programa encerra quando o usuário informa o texto SAIR."""
Info_Cliente = []
Cliente_SexFeminino_Alu7dias = []
Media_km = 0
Cont = 0
Exit = ''
while Exit != 'Sair':
    while True:
        print("\nPara sair basta digitar 'SAIR'")
        Nome_Cliente = input("\nDigite o nome do cliente: ").title()
        if Nome_Cliente == 'Sair':
            Exit = 'Sair'
            print("\n")
            print("-=-=-" * 13)
            break
        Sexo_Cliente = input("\n(F - Feminino, M - Masculino)\n"
                             "Digite o sexo do cliente: ").upper()
        if Sexo_Cliente not in ['F', 'M']:
            print("OPS! Algo deu errado na identificação do sexo do cliente. Tente novamente.")
            break
        Placa_Carro = input("\nNumero da placa do carro que será alugado: ").upper()
        Letras_Placa = Placa_Carro[:3]
        Numeros_Placa = Placa_Carro[3:]
        if 7 < len(Placa_Carro) > 7 or not Letras_Placa.isalpha() or not Numeros_Placa.isnumeric():
            print("OPS! Algo deu errado na identificação da placa do veiculo. Tente novamente.")
            break
        try:
            Qtd_Km_Contratado = float(input("\nDigite a quantidade de quilometros contratados: "))
            Qtd_Dias_Contratados = int(input("\nDigite a quantidade de dias contratados: "))
        except ValueError:
            print("OPS! Só pode ser colocar apenas números nesta alternativa. Tente novamente.")
            break

        if Sexo_Cliente == 'F' and Qtd_Dias_Contratados > 7:
            Info1 = f'Cliente: {Nome_Cliente}\n' \
                    f'Quantidade de dias contratados: {Qtd_Dias_Contratados}'
            Cliente_SexFeminino_Alu7dias.append(Info1)
        Valor_Total = (Qtd_Km_Contratado * 70) + (Qtd_Dias_Contratados * 0.10)
        Cont += 1
        Media_km += Qtd_Km_Contratado * 70
        Info2 = f'Cliente nº{Cont}: {Nome_Cliente}\n' \
                f'Placa: {Placa_Carro}\n' \
                f'Qtd dias: {(Qtd_Dias_Contratados * 0.1):.2f} + Qtd Km: {Qtd_Km_Contratado * 70}\n' \
                f'Valor total: {Valor_Total}'
        Info_Cliente.append(Info2)

print("Quantidade de Clientes: ")
if len(Info_Cliente) != 0:
    for i in range(len(Info_Cliente)):
        print(f"{Info_Cliente[i]}\n")
else:
    print("Ocorreu algum erro ou não nos foi informado nenhum dado...")
print("-=-=-" * 13)

print("Media Total de Quilimetros: ")
if Media_km != 0:
    print(f'{(Media_km / Cont):.2f}\n')
else:
    print("Sem dados adquiridos para fazer a Média de quilometros...")
print("-=-=-" * 13)

print("Clientes do Sexo feminino que possui Contrato de dias maior que 7: ")
if len(Cliente_SexFeminino_Alu7dias) != 0:
    for j in range(len(Cliente_SexFeminino_Alu7dias)):
        print(f"{Cliente_SexFeminino_Alu7dias[j]}\n")
else:
    print("Ocorreu algum erro ou não nos foi informado nenhum dado...")
print("-=-=-" * 13)