"""5. Dado um vetor de inteiros, insira valores neste vetor. Em seguida, informe o
percentual de números pares. Imprima o resultado no console.
Ex.: [2,0,1,5,9,7,6]
Resposta: 42.8%"""

Vetor = [2, 0, 1, 5, 9, 7, 6]
T_Pares = 0
for i in range(0, len(Vetor)):
    if Vetor[i] % 2 == 0:
        T_Pares += 1
print((T_Pares / len(Vetor)) * 100)
