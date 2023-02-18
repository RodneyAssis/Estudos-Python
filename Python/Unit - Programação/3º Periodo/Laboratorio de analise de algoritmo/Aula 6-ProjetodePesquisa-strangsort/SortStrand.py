Lista = [10, 5, 30, 40, 2, 4]
ListaSubs = []
ListaOrdenada = []

aux = 0
posicion = 0


while True:
    if Lista[aux] < Lista[posicion+1]:
        ListaOrdenada.insert(aux, Lista[aux])
        print(ListaOrdenada)
        aux += 1
        posicion = 0
    elif Lista[aux] > Lista[posicion+1]:
        posicion += 1
    print(ListaOrdenada)
