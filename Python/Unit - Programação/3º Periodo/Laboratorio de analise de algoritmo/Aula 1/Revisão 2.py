from random import randint

"""2. Crie um algoritmo que defina um vetor de elementos inteiros de tamanho 7, insira
valores aleatórios neste vetor e calcule a soma dos elementos pares do vetor seguida
pelo valor da soma dos elementos ímpares. Imprima o resultado no console.
Ex.: [2,0,1,5,9,7,6]
Resposta: 8-22"""

Vetor = []

Par = 0
Impar = 0
for i in range(0, 7):
    Random = randint(1, 100)
    Vetor.append(Random)
    if Vetor[i] % 2 == 0:
        Par += Vetor[i]
    else:
        Impar += Vetor[i]

print("Vetor:", Vetor)
print("Par:", Par)
print("Impar:", Impar)

