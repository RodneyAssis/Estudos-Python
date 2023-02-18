#10 - Uma empresa decide aplicar descontos nos preços dos seus produtos de acordo com o preço atual de cada um. Faça um
#     programa em Python para ler a descrição do produto e seu preço atual. Calcule o desconto de acordo com a tabela
#     abaixo e imprima: descrição do produto, preço atual, valor do desconto e o novo preço.

#               Preço Atual    |     Desconto
#                  30.00       |   Sem Desconto
#              Entre 30 e 100  |       10%
#             Entre 100 e 500  |       15%
#                Acima 500     |       20%
preço=0

while True:
    produto = int(input("Digite o valor do produto:"))
    if produto==0:
        break
    preço=preço+produto
print("\nValor do produto (sem desconte):",preço)

if (preço > 30) and (preço <= 100):
    des=preço-(preço*0.10)
    print(preço,"mais 10% desconto")
    print("Valor a ser pago:",des)
elif (preço > 100) and (preço <= 500):
    des=preço-(preço*0.15)
    print(preço,"{} mais 15% desconto")
    print("Valor a ser pago:",des)
elif preço > 500:
    des=preço-(preço*0.20)
    print(preço,"{} mais 20% desconto")
    print("Valor a ser pago:",des)