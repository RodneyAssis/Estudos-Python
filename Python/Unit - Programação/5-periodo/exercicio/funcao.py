def f(x):
    # Calor especifico
    return - 1.1 + 0.99403 + (1.671 * 10 ** -4) * x + (9.7215 * 10 ** -8) * x ** 2 \
           - (9.5838 * 10 ** -11) * x ** 3 + (1.9520 * 10 ** -14) * x ** 4


def df(x, erro):
    return (f(x + erro) - f(x)) / erro


def modulo(x):
    if x > 0:
        return x
    else:
        return -x


def dataframe(dados, xa, xb, xmed, fxa, fxb, fxm, situacao):
    # Dados armazenados para a tabela
    return dados['xa'].append(xa), dados['xb'].append(xb), dados['xm'].append(xmed), \
           dados['fxa'].append(fxa), dados['fxb'].append(fxb), dados['fxm'].append(fxm), \
           dados['SITUAÇÃO'].append(situacao)


def dataframe1(dados1, xa, fx, xb, situacao):
    # Dados armazenados para a tabela
    return dados1['xa'].append(xa), dados1['fx'].append(fx), \
           dados1['xb'].append(xb), dados1['SITUAÇÃO'].append(situacao)
