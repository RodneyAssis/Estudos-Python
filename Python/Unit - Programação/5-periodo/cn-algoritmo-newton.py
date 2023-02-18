import funcao
import math


def f(x):
    return 2 * x * math.exp(x) - 3


def df(x):
    return (f(x + erro) - f(x)) / erro


x_inicio = int(input("Digite no nome: "))
erro = float(input("Digite a raiz de precisão: "))

x_final = 0

while True:
    if funcao.modulo(f(x_inicio)) < erro:
        print("FIM")
        print(f(x_inicio))
        break
    else:
        print("CONTINUE")
        x_final = x_inicio - f(x_inicio) / df(x_inicio)

        if funcao.modulo(f(x_final)) < erro:
            print("RAIZ ENCONTRADA!")
            print(f"Xf = {x_final}\n"
                  f"erro = {x_inicio - x_final}")
            break
        else:
            print("RETORNANDO AO INICIO")
            print(f"Xi   {x_inicio}\n"
                  f"F(x) {f(x_inicio)}\n"
                  f"dF(x) {df(x_inicio)}\n"
                  f"xi+1 {x_final}")
            print("Erro: ", x_inicio - x_final)
            x_inicio, x_final = x_final, x_inicio
