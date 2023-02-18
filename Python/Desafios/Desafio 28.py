from random import randint
from time import sleep
acertos = 0
erros = 0
print("-=-"*10)
print(" "*4,"Jogo de Adivinhação")
print("-=-"*10)

while True:
    print("")
    Numero = int(input("Digite um número de 0 à 5: "))
    print("\033[1:32mPROCESSANDO...\033[m")
    sleep(1)
    a = randint(0, 5)
    if Numero == a:
        print("Você acertou!!")
        print("Estava pensamos no número {}!!!".format(a,Numero))
        acertos += 1
    else:
        print("Você errou!!")
        print("Eu pensei no número {}, você disse {}".format(a,Numero))
        erros += 1
    x=str(input("Deseja continuar? "))
    if x == "n":
        break
print(f"Acertos: {acertos} \nErros: {erros}")