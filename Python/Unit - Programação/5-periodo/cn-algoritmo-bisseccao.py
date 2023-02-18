from math import exp
import funcao
import numpy
import matplotlib.pyplot as plt

xa = float(input("Digite o valor do primeiro intervalo: "))
xb = float(input("Digite o valor do segundo intervalo: "))
p = float(input("Valor de precisão: "))

x = 0
cont = 0

lista = [[], [], [], [], [], [], []]

while True:
    cont += 1
    x = xa
    fxa = 2 * x * exp(x) - 3

    x = xb
    fxb = 2 * x * exp(x) - 3

    print(f"Iteração: {cont}")
    print("Valor de Xa:", xa)
    print("Valor de Xb:", xb)
    print("Função de Xa:", fxa)
    print("Função de Xb:", fxb)
    lista[0].append(xa)
    lista[1].append(xb)
    lista[2].append(fxa)
    lista[3].append(fxb)
    if fxa * fxb < 0:
        xm = (xa + xb) / 2
        x = xm
        fxm = 2 * x * exp(x) - 3
        print("Função do ponto medio: ", fxm)
        lista[4].append(fxm)
        if funcao.modulo(fxm) < p:
            lista[5].append(f"Criterio de ponto medio, valor aproximado: "
                            f"\nPonto medio: {xm}"
                            f"\nValor de Precisão: {p}")
            break
        else:
            if fxa * fxm < 0:
                lista[5].append("Xb vai receber o ponto medio")
                print("Xb vai receber o ponto medio")
                xb = xm
            else:
                lista[5].append("Xa vai receber o ponto medio")
                print("Xa vai receber o ponto medio")
                xa = xm
        if funcao.modulo(fxm) < p:
            print("Raiz encontrada!", fxm, p)
            break
    else:
        break


for i in range(0, len(lista[0])):
    print(f"\n{i+1} iteração"
          f"\nValor Xa:  {lista[0][i]:.4f}"
          f"\nValor Xb:  {lista[1][i]:.4f}"
          f"\nValor Fxa: {lista[2][i]:.4f}"
          f"\nValor Fxb: {lista[3][i]:.4f}"
          f"\nValor Fxm: {lista[4][i]:.4f}"
          f"\n{lista[5][i]}")
