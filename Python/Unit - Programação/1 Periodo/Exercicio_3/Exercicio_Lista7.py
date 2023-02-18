from random import randint

Lista=[]
cont= 0

print("Lista:")
for i in range(0,128):
    x = randint(1,150)
    cont = cont + 1
    Lista.append(x)
    print(f"|nº{cont} = {Lista[i]}",end="")
print("")

Chave= randint(1,150)
print("Chave gerada:",Chave)

cont = 0

for j in range(0,128):
    cont = cont + 1
    if Chave/Lista[j] == 1:
        print(f"O numero chave está na posição: {cont}")
        break