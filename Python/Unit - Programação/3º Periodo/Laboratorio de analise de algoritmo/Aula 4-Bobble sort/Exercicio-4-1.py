from random import randint
"""
2. Utilizando uma linguagem de programação de sua preferência, implementar o
Bubble Sort.
a. Nesta questão, o algoritmo não pode ter dois loops ou “laços de repetição”.
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


comp = 0  # RECEBE A POSIÇÃO DA LISTA;
aux = 1  # RECEBE UMA A POSIÇÃO A FRENTE DA LISTA;
cont = 0

print(f"Lista Recebida: {Lista}")

while True:
    if aux > len(Lista) - 1:
        # CONDIÇÃO PARA QUANDO AS VARIAVEIS JÁ ESTIVEREM NA ULTIMA POSIÇÃO ASSIM RESETANDO SUAS POSIÇÕES PARA LOCALIZAR
        # AS DEMAIS POSIÇÕES NÃO ORDENADAS;
        cont += 1  # CONTAGEM DE VEZES QUE ENTROU NESSA CONDIÇÃO
        aux = 1
        comp = 0
        if cont == len(Lista):
            # ASSIM QUE A VARIAVEL ATINGIR UM VALOR SEMELHANDO A QUANTIDADE DE ELEMENTOS DE UMA LISTA, FINALIZA O
            # SISTEMA MOSTRANDO ASSIM O RESULTADO;
            break

    if Lista[aux] < Lista[comp]:
        # CONDIÇÃO ONDE A POSIÇÃO A FRENTE É MENOR QUE SUA POSIÇÃO ANTERIOR FAZENDO A TROCA DE POSIÇÕES ORDENANDO DE
        # FORMA CRESCENTE A LISTA;
        Lista[comp], Lista[aux] = Lista[aux], Lista[comp]
    elif Lista[aux] > Lista[comp]:
        # CONDIÇÃO QUANDO A POSIÇÃO A FRENTE É MAIOR QUE A SUA POSIÇÃO ANTERIOR É REALIZADO UM AVANÇO NAS DEMAIS
        # POSIÇÕES CONTINUANDO O PROCESSO;
        aux += 1
        comp += 1
    elif Lista[aux] == Lista[comp]:
        # CONDIÇÃO QUANDO A POSIÇÃO A FRENTE É IGUAL A POSIÇÃO ANTERIOR É REALIZADO UM AVANÇO NAS DEMAIS POSIÇÕES
        # CONTINUANDO O PROCESSO;
        aux += 1
        comp += 1

# SAINDO DO LAÇO DE REPETIÇÃO ONDE AMOSTRA A LISTA DE FORMA ORDENADA E CRESCENTE;
print(f"Lista ordenado: {Lista}")
