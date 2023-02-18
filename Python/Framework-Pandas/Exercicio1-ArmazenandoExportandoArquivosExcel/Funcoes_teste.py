"""Lista_Matrix = []
for i in range(10):
    Lista_Matrix.append([])
    for j in range(5):
        Lista_Matrix[i] += ['X']

for k in range(len(Lista_Matrix)):
    print(Lista_Matrix[k])"""


def add_aresta(x, y):
    grafo[x].append(y)


def most_list():
    for i in range(vertice):
        print(f"{i}:", end=" ")
        for j in grafo[i]:
            print(f'{j} ->', end=" ")
        print("")

vertice = 6
grafo = [[] for i in range(vertice)]

add_aresta(0, 1)
add_aresta(0, 2)
add_aresta(0, 3)
add_aresta(0, 4)
add_aresta(0, 5)
add_aresta(1, 2)
add_aresta(3, 4)
add_aresta(5, 0)

print(most_list())