from random import randint
"""3. Dado um vetor com elementos inteiros, insira valores aleatórios neste vetor. Em
seguida, crie outro vetor que contenha os mesmos elementos inteiros do primeiro vetor,
só que na ordem inversa à inserida. Imprima o resultado no console.
Ex.: [2,0,1,5,9,7,6]
Resposta: [6,7,9,5,1,0,2]"""

Vetor = [2, 0, 1, 5, 9, 7, 6]
for i in range(0, 7):
    Random = randint(1, 100)
    Vetor.append(Random)
Novo_Vetor = Vetor.copy()
Novo_Vetor.reverse()
print("Novo Vetor", Novo_Vetor)
