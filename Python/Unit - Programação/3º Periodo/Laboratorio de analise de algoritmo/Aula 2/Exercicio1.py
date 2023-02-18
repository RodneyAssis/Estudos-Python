import math
"""
Exercicio de analise de algoritmo

Calcular o tempo de execução de um computador, cujo o poder é de processamento
é de 1 bilhão de instruções por segundo, e pretende ordenar 40 milhões de números:

1- Cenario A:
    Utilizar um algoritmo por intercalação (nlogn)

2- Cenario B:
    Utilizar um algoritmo por inserção (2n^2)
"""

# Cenario A Utilizando Ordenação por intercalação:
print("----------------------CENARIO A----------------------")

# Dados do Algoritmo:
n = 4 * (10**7)  # 40.000.000
Limitador_Casas_Decimais = int(n / 10 ** 6)
print(f"Numero de ordenação: {Limitador_Casas_Decimais} milhões")
Ordem_Intercalada = n * math.log10(n)
print(f"Valor de instruções realizadas pelo algoritmo: {round(Ordem_Intercalada)}")

# Dados do Computador:
print()
Num_Instrucoes = 10**9  # 1.000.000.000
Limitador_Casas_Decimais = int(Num_Instrucoes / 10 ** 9)
print(f"{Limitador_Casas_Decimais} bilhão de instruções por segundo")

# Resultado Matematicamente:
Resultado = Ordem_Intercalada/Num_Instrucoes

print(f"Resultado da analise: {Resultado:.1f}")

# Cenario B Utilizando Ordenação por inserção :
print("\n----------------------CENARIO A----------------------")

# Dados do Algoritmo:
n = 4 * (10**7)  # 40.000.000
Limitador_Casas_Decimais = int(n / 10 ** 6)
print(f"Numero de ordenação: {Limitador_Casas_Decimais} milhões")
Ordem_Insercao = 2 * n**2
print(f"Valor de instruções realizadas pelo algoritmo: {round(Ordem_Insercao)}")

# Dados do Computador:
Num_Instrucoes = 10**9  # 1.000.000.000
Limitador_Casas_Decimais = int(Num_Instrucoes / 10 ** 9)
print(f"\n{Limitador_Casas_Decimais} bilhão de instruções por segundo")

# Resultado Matematicamente:
Resultado = Ordem_Insercao/Num_Instrucoes
print(f"Resultado da analise: {int(Resultado)}")
