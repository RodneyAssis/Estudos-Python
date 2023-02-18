q=1
w=2
e=3
r=4
Cor={"Branco":"\033[1;30m", "Vermelho":"\033[0;31m", "Verde":"\033[1;32m",
     "Amarelo":"\033[0;33m", "Azul":"\033[0;34m"}
while True:
    Valor = float(input("Digite o valor total dos produtos: "))
    print("[1-À vista Dinheiro/Check] [2-À vista Cartão] [3-Em até 2x] [4-De 3x ou mais]")
    Tip_Pag = float(input("Escolha o tipo de pagamento: "))

    if Tip_Pag == 1:
        Option=int(input("\n(1-Dinheiro) (2-Check)\nTipo de pagamento: "))
        Desc= Valor-(Valor*0.1)
        print("\n{}Desconto de 10%.\nValor a ser pago:{} R${:.2f}".format(Cor["Verde"],Cor["Amarelo"],Desc))
    elif Tip_Pag == 2:
        Desc= Valor-(Valor*0.05)
        print("\n{}Desconto de 5%.\nValor a ser pago:{} R${:.2f}".format(Cor["Verde"],Cor["Amarelo"],Desc))
    elif Tip_Pag == 3:
        print("\n{}Valor a ser pago:{} 2x R${:.2f}".format(Cor["Amarelo"],Cor["Branco"],Valor/2))
    elif Tip_Pag == 4:
        x=int(input("\nDigite até quantas vezes deseja colocar: "))
        Desc= Valor+(Valor*0.2)
        print("\n{}Adicional de 20%.{}\nValor a ser pago será de: {}x {}R${:.2f}"
              .format(Cor["Vermelho"],Cor["Amarelo"],x,Cor["Vermelho"], Desc/x))

    if (Tip_Pag != q) and (Tip_Pag != w) and (Tip_Pag != e) and (Tip_Pag != r):
        print("<Erro!> Não existe esse comando no sistema, tente novamente.\n")
    else:
        break
