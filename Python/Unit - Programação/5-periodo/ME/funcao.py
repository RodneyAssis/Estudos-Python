from math import *

def f(x):
    return 9 * exp(-x) * sin(2*pi*x)


def df(x, erro):
    return (f(x + erro) - f(x)) / erro


def modulo(x):
    if x > 0:
        return x
    else:
        return -x