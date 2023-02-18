import pandas as pd
import random

dados = []
coluna = ['coisas']
cont = 0
while len(dados) < 3:
    val = random.choice(['caixa', 'carro', 'bostas', 'comida', 'coisinhas'])
    dados.append(val)


tabela = pd.DataFrame(data=dados, columns=coluna)

print(tabela)