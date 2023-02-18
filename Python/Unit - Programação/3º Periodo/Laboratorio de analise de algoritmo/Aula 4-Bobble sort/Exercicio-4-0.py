from random import randint
"""
1. Utilizando uma linguagem de programação de sua preferência, implementar o
Bubble Sort.
a. Deve-se comentar o que cada linha implementada significa (ou executa).
"""

Lista = []
Opcao = int(input("1-Opção por meio de aleatoriedade\n"  # CONDIÇÃO SELECIONADA POR MEIO DO USÚARIO
                  "2-Opção Manual da lista\n"
                  "Escolha uma das opções: "))

if Opcao == 1:  # OPÇÃO POR MEIO DE ALEATORIEDADE;

    # QUANTIDADE DE NÚMEROS NA LISTA;
    Qtd_Num_Lista = int(input("Escolha a quantidade de números armazenar na lista: "))
    # ESCOLHA DE NUMEROS ALEATORIOS(1 ATÉ A 'OPÇÃO DO USUARIO')
    Numeros = int(input("Escolha o numero maximo de seleção: "))
    while len(Lista) != Qtd_Num_Lista:
        Aleatorio = randint(1, Numeros)
        Lista.append(Aleatorio)

elif Opcao == 2:  # OPÇÃO DE ESCOLHA MANUAL DA LISTA;
    # QUANTIDADE DE NÚMEROS NA LISTA;
    Qtd_Num_Lista = int(input("Escolha a quantidade de números armazenar na lista: "))
    for i in range(Qtd_Num_Lista):
        Escolha = int(input(f"Escolha um número para {i+1}º posição da lista: "))
        Lista.append(Escolha)

print(f"\nNumeros recebidos para a lista: {Lista}")
for j in range(len(Lista)-1):  # APLICANDO A REPETIÇÃO DOS NÚMEROS ATÉ O MOMENTO EM QUE A LISTA JÁ ESTEJA ORDENADA;
    for i in range(len(Lista)-1):  # MAPEANDO O A LISTA E TROCANDO AS POSIÇÕES EM ORDEM CRESCENTE;
        if Lista[i] > Lista[i+1]:  # REALIZAÇÃO DA TROCA DAS POSIÇÕES DOS ELEMENTOS;
            Lista[i+1], Lista[i] = Lista[i], Lista[i+1]

print(f"Lista ordenada: {Lista}")
