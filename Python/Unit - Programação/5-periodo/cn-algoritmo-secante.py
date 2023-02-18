import math
import funcao


def func(val):
    fx = 2 * val * math.exp(val) - 3
    return fx


ximi = -134.72
xi = -30
p = 0.01

if funcao.modulo(func(ximi)) < p or funcao.modulo(func(xi)) < p:
    print("Fim")
else:
    print("Continue")
