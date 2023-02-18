"""A LOTOFACIL consiste na extração de 15 números aleatórios diferentes, no universo de 01 a 25. Você
marca entre 15 a 18 números, dentre os 25 disponíveis no volante, e fatura o prêmio se acertar 11, 12,
13, 14 ou 15 números. Pode ainda deixar que o sistema escolha os números para você por meio da
Surpresinha. Considerando estas informações, faça um programa em Python para:
a) Solicitar ao usuário a quantidade de dezenas que ele deseja marcar na primeira aposta (entre 15 e 18 números).
Caso o usuário informe uma quantidade de dezenas fora do intervalo válido, o programa deve solicitar nova digitação,
tantas vezes quantas forem necessárias;
b) Solicitar ao usuário informar os números da primeira aposta (dezenas de 01 a 25, sem repetição). Caso o usuário
informe um número repetido, o programa deverá apresentar uma mensagem “Número repetido” e solicitar nova
digitação. Assim como se o usuário informar um número fora do intervalo válido, o programa deverá apresentar uma
mensagem “Dezena inválida” e solicitar nova digitação.
c) Gerar aleatoriamente duas apostas, com 18 números, usando a “Surpresinha”.
d) Simular o resultado (15 dezenas sorteadas) de um concurso da Lotofácil;
e) Imprimir (em ordem crescente) as dezenas da primeira aposta, das duas apostas (surpresinha) e do resultado do
concurso da Lotofácil simulado."""
import random

condicao = 0
LOTO_USUARIO = []
while condicao not in [15, 16, 17, 18]:
    try:
        Loto_1 = int(input("\nDigite quantos numeros deseja marcar na primeira aposta entre 15 à 18: "))
        condicao = Loto_1
    except ValueError or OverflowError:
        print("\nErro! Só pode ser selecionado apenas números inteiros.\n")

while True:
    try:
        while len(LOTO_USUARIO) != condicao:
            Num_1Aposta = int(input("\nEscolha números entre 1 à 25: "))
            if Num_1Aposta > 25 or Num_1Aposta < 1:
                print("\nPor favor, selecione os números entre 1 e 25.")
            elif Num_1Aposta in LOTO_USUARIO:
                print("\nEste número encontra-se selecionado. Por favor escolha outro número.")
            else:
                LOTO_USUARIO.append(Num_1Aposta)

        print(f"\nNúmeros escolhidos: {LOTO_USUARIO}")
        Corretor = int(input("\n[1 - SIM, 2 - NÃO]\nDeseja refazer sua aposta? "))
        if Corretor == 1:
            LOTO_USUARIO = []
        else:
            break
    except ValueError or OverflowError:
        print("\nErro! Só pode ser selecionado apenas números inteiros.")

# SISTEMA DE SURPRESINHA.
condicao_1 = 0
while condicao_1 not in [1, 2]:
    try:
        Condicao_Surpresinha = int(input("\n[1 - SIM, 2 - NÃO]\n"
                                         "Deseja adicionar mais duas apostas aleatoriamente"
                                         "\npelo sistema por meio de 'Surpresinhas'? "))
        condicao_1 = Condicao_Surpresinha
    except ValueError or OverflowError:
        print("\nErro! Só pode ser selecionado apenas números inteiros.")

# NÚMEROS ESCOLHIDOS ALEATORICAMENTES PELA LOTOFACIL.
NUM_LOTOFACIL = []
while len(NUM_LOTOFACIL) != 15:
    numero_loto = random.randint(1, 25)
    if numero_loto not in NUM_LOTOFACIL:
        NUM_LOTOFACIL.append(numero_loto)
        NUM_LOTOFACIL.sort()

print(f"\nNúmeros da LOTOFACIL:", end=" ")
for j in range(len(NUM_LOTOFACIL)):
    print(f"{NUM_LOTOFACIL[j]}", end=" ")

# NÚMEROS ESCOLHIDOS PELO PELO USUARIO.
print("\n\n", 12 * "-=", "PRIMEIRA APOSTA", "=-" * 12)
LOTO_USUARIO.sort()
print("\nNúmeros do Usuario:  ", end=" ")
for i in range(len(LOTO_USUARIO)):
    print(f"{LOTO_USUARIO[i]}", end=" ")

cont = 0
for k in LOTO_USUARIO:
    if k in NUM_LOTOFACIL:
        cont += 1
print("\nNumero de acertos:", cont)

if condicao_1 == 1:

    # NÚMEROS DA PRIMEIRA SURPRESINHA.
    NUM_SURPRESINHA1 = []
    while len(NUM_SURPRESINHA1) != condicao:
        surpresinha1 = random.randint(1, 25)
        if surpresinha1 not in NUM_SURPRESINHA1:
            NUM_SURPRESINHA1.append(surpresinha1)
            NUM_SURPRESINHA1.sort()

    print("\n", 12 * "-=", "PRIMEIRA SURPRESINHA", "=-" * 12)
    print(f"\nNúmeros da 1º surpresinha:", end=" ")
    for i in range(len(NUM_LOTOFACIL)):
        print(f"{NUM_SURPRESINHA1[i]}", end=" ")

    cont1 = 0
    for k in NUM_SURPRESINHA1:
        if k in NUM_LOTOFACIL:
            cont1 += 1
    print("\nNumero de acertos:", cont1)

    # NÚMEROS DA SEGUNDA SURPRESINHA.
    NUM_SURPRESINHA2 = []
    while len(NUM_SURPRESINHA2) != condicao:
        surpresinha2 = random.randint(1, 25)
        if surpresinha2 not in NUM_SURPRESINHA2:
            NUM_SURPRESINHA2.append(surpresinha2)
            NUM_SURPRESINHA2.sort()

    print("\n", 12 * "-=", "SEGUNDA SURPRESINHA", "=-" * 12)
    print(f"\nNúmeros da 2º surpresinha:", end=" ")
    for i in range(len(NUM_LOTOFACIL)):
        print(f"{NUM_SURPRESINHA2[i]}", end=" ")

    cont2 = 0
    for k in NUM_SURPRESINHA2:
        if k in NUM_LOTOFACIL:
            cont2 += 1
    print("\nNumero de acertos:", cont2)
