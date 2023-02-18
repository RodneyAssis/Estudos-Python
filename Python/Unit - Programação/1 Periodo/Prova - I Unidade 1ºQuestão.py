# 1º Questão
# Nome do Aluno: Rodney Assis Matos Furtado
# Nº de Matricula: 1201131119
cont = 0
Total_Acumulado = 0
TotalPrdMasc = 0
Valor = 0
Quanti = 0
QuantM = 0
Aci200 = 0
Maior = 0
NomeM = ""
Menor = 999999999999
NomeMe = ""
while True:
    RCC = int(input("Digite o Codigo do Cliente: "))
    Nome = str(input("Digite o seu nome: "))
    print("[M - Masculino / F - Feminino]")
    Sexo = str(input("Digite o seu Sexo: ")).capitalize()

    if Sexo == "M":
        Produto = float(input("Digite o valor do produto: "))
        Quant = int(input("Digite a quantidade de produtos: "))
        V_produto = Produto * Quant
        if V_produto >= 200:
            Aci200 = Aci200 + 1
        Total_Acumulado = Total_Acumulado + V_produto
        TotalPrdMasc = TotalPrdMasc + V_produto
        QuantM = QuantM + 1
        Quanti = Quanti + 1
    elif Sexo == "F":
        Produto = float(input("Digite o valor do produto: "))
        Quant = int(input("Digite a quantidade de produtos: "))
        V_produto = Produto * Quant
        if V_produto >= 200:
            Aci200 = Aci200 + 1
        Total_Acumulado = Total_Acumulado + V_produto
        Quanti = Quanti + 1
        if Produto < Menor:
            NomeMe = Nome
            Menor = Produto
    else:
        print("Erro!!")
        break
    print("[S - Sim / N - Não]")
    Close = str(input("Deseja encerrar o expediênte? ")).capitalize()
    cont = cont + 1
    if Close == "S":
        break
    elif Close == "N":
        print("")
    else:
        print("ERRO!")
        break

print("")
print(f"Número de cliêntes: {cont}")
print("Total dos Valores:", Total_Acumulado)  # Letra A
if QuantM > 0:
    Media = TotalPrdMasc / QuantM
    print("Media de produtos dos clientes do sexo masculino: ", Media)  # Letra B
else:
    print("Não possui cliêntes do sexo masculino.")  # Letra B
Porcent = (Aci200 / Quanti) * 100
print(f"O produto com menor preço dos clientes do sexo feminino é {NomeMe} que gastou R${Menor:.2f}")  # Letra C
print(f"Porcentual de clientes que compraram acima de 200: {Porcent:.1f}%")  # Letra D

