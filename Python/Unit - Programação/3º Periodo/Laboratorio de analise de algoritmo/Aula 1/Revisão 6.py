"""6. Dado um vetor com elementos inteiros, insira valores neste vetor. Em seguida, crie
outro vetor que contenha os mesmos elementos inteiros do primeiro vetor, só que em
ordem decrescente. Imprima o resultado no console.
Ex.: [2,0,1,5,9,7,6]
Resposta: [9,7,6,5,2,1,0]"""

Vetor = [2, 0, 1, 5, 9, 7, 6]
Vetor.sort(reverse=True)
Novo_Vetor = Vetor
print(Novo_Vetor)
