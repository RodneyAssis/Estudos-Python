import pandas as pd
from funcao import *

"""
1) Nas engenharias frequentemente a termodinâmica é utilizada para diferentes finalidades tais
como a determinação de propriedades térmicas de materiais. O polinômio abaixo pode s er
usado para relacionar o calor específico do ar seco à pressão nula, Cp kJ/(Kg.K) a uma dada
temperatura T (K).

Cp = 0,99403 + 1,671 × 10−4T + 9,7215 × 10−8T^2 − 9,5838 × 10−11T^3 + 1,9520 × 10−14T^4

Use os métodos numéricos vistos para determinar a temperatura que corresponde a um calor
específico de 1,1 kJ/(Kg.K).
"""

# DATAFRAME
dados = {'xa': [], 'xb': [], 'xm': [], 'fxa': [], 'fxb': [], 'fxm': [], 'SITUAÇÃO': []}

# Variaveis
Tinicial = -600
Tfinal = -500
xm = 0
p = 10 ** -10
""""
# METODO DA BISSECÇÃO
while True:
    # VALOR INICIAL DEFINIDO PARA A TABELA.
    if xm == 0:
        dataframe(dados, Tinicial, Tfinal, xm, Tinicial, Tfinal, xm, 'INICIAL')

    # SE O MODULO DE F(xm) for menor que a raiz, ENCERRAR O CODIGO.
    if f(Tinicial) * f(Tfinal) < 0:
        xm = (Tinicial + Tfinal) / 2

        # SE O MODULO DE F(xm) for menor que a raiz, ENCERRAR O CODIGO, POIS A FOI ENCONTRADO UM VALOR MENOR QUE A RAIZ
        # DEFINIDA
        if modulo(f(xm)) < p:
            print("valor da aproximação da raiz foi menor que que o valor da Raiz")
            print(f"raiz: {p}\n media entre os intervalos: {modulo(f(xm))}")
            dataframe(dados, Tinicial, Tfinal, xm, Tinicial, Tfinal, xm, 'FIM')
            break

        else:
            # Tfinal vai receber o valor de xm
            if f(Tinicial) * f(xm) < 0:
                Tfinal = xm

            # Tinicial vai receber o valor de xm
            else:
                Tinicial = xm

            # CRITERIO DE PARADA SE O INTERVALO FINAL - INTERVALO INICIAL FOR MENOR QUE
            if modulo(Tfinal - Tinicial) < p:
                print(f"Raiz encontrada: {modulo(f(xm))}\n"
                      f"Raiz: {p}")
                dataframe(dados, Tinicial, Tfinal, xm, Tinicial, Tfinal, xm, 'RAIZ ENCONTRADA')

                break
            else:
                print("Retorna a calcular a nova media\n")
                dataframe(dados, Tinicial, Tfinal, xm, Tinicial, Tfinal, xm, 'CONTINUE')

    else:
        print("Gerar Novo intervalo!\n")
        break

tabela = pd.DataFrame(dados)
print(tabela)


"""


"""# METODO DE NEWTON
dados1 = {'xa': [], 'fx': [], 'xb': [], 'SITUAÇÃO': []}
cont = 0
while True:
    if cont == 0:
        dataframe1(dados1, Tinicial, f(Tinicial), 0, "INICIO")
        print("inicio")
    if modulo(f(Tinicial)) < p:
        print(f"x0 {Tinicial} é igual a raiz {p}")
        dataframe1(dados1, Tinicial, f(Tinicial), Tfinal, "FIM")
        break
    else:
        Tfinal = Tinicial - (f(Tinicial)/df(Tinicial, p))

    if modulo(f(Tfinal)) < p and modulo(Tfinal - Tinicial) < p:
        print(f"{modulo(Tfinal - Tinicial)} raiz {p}\n"
              f"raiz encontrada")
        dataframe1(dados1, Tinicial, f(Tinicial), Tfinal, "FIM")
        break
    else:
        Tinicial = Tfinal
        dataframe1(dados1, Tinicial, f(Tinicial), Tfinal , "CONTINUE")
        print("Continue")
        cont += 1

tabela = pd.DataFrame(dados1)
print(tabela)
"""

print(f(4000))

print(df(4000, 0.000000001))

print((f(4000 + 0.000000001) - f(4000))/0.000000001)