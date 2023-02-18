# 1. Desenvolver um algoritmo que represente o grafo da figura a baixo:
#
#  a) [0,5] Em memória, como uma matriz de adjacência.
#  b) [0,5] Criar um método/função para iterar em cada elemento da matriz e imprimir no console.

def matrix_adj():
    matrixx = []
    for i in range(6):
        matrixx.append([])
        for j in range(6):
            matrixx[i] += ['#']
    return matrixx


caracteres = ['Mar', 'Nil', 'The', 'Cla', 'Gae', 'Nan']

matrix = matrix_adj()

matrix[0][1] = 'V'  # Marcio > Nilda
matrix[1][2] = 'V'  # Nilda > Theo
matrix[2][0] = 'V'  # Theo > Marcio
matrix[0][3] = 'V'  # Marcio > Clara
matrix[3][4] = 'V'  # Clara > Gael
matrix[4][0] = 'V'  # Gael > Marcio
matrix[0][5] = 'V'  # Marcio > Nanda
matrix[5][0] = 'V'  # Nanda > Marcio

print("\nMatrix Adjecente")
print("     Mar, Nil, The, Cla, Gae, Nan")
for k in range(len(matrix_adj())):
    print(f"{caracteres[k]} {matrix[k]}")


# c) [1,0] Em memória, como uma lista de adjacência.
# d) [1,0] Criar um método/função para iterar em cada elemento da matriz e imprimir no console.

def add_aresta(x, y):
    grafo[x].append(y)


def most_list():
    for d in range(vertice):
        print(f"{d}:", end=" ")
        for j in grafo[d]:
            print(f'{j} -', end=" ")
        print("")


print("\n Lista Adjecente")
vertice = 6
grafo = [[] for f in range(vertice)]

add_aresta(0, 1)
add_aresta(1, 2)
add_aresta(2, 0)
add_aresta(0, 3)
add_aresta(3, 4)
add_aresta(4, 0)
add_aresta(5, 0)
add_aresta(0, 5)

print(most_list())


# 2 - [1,0] Desenvolver um método/função que receba como parâmetro uma matriz de adjacência qualquer, calcule e
# retorne o valor de sua complexidade (n2).

def calculo(matrix):
    n = len(matrix)
    calc = 0
    for i in range(n):
        for j in range(n):
            calc += n * j
    return calc


print("\nComplexidade n^2")
print(calculo(matrix))
