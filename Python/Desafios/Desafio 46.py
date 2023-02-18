from time import sleep
Cor={"Branco":"\033[0;30m","Vermelho":"\033[1;31m","Verde":"\033[1;32m"}
X = 10
for Contagem in range (0,10+1):
    print("Contagem regressiva em: {}{}{}".format(Cor["Vermelho"],X,Cor["Branco"]))
    X = X - 1
    sleep(1)
print("{}Soltar Fogos!!".format(Cor["Verde"]))