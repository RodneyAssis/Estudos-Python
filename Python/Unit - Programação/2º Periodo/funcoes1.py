def Dicionario(Dicionario):
    Chave = list(Dicionario.keys())
    Valor = list(Dicionario.values())

    X = min(Valor)
    Menor = Valor.index(X)
    return f"A menor particula de ser observada é a {Chave[Menor]} com probabilidade de {Valor[Menor]*100:.2f}%"
