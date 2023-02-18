import random
import string


def Escolha_Usuario(array):
    Opcao = 0
    while not Opcao == 1 or Opcao == 2:
        Opcao = int(input("1- Fazer a Lista manualmente\n"
                          "2- Fazer uma lista randomicamente\n"
                          "Escolha uma das alternativas:"))

        Qtd_Num_List = int(input("Digite a quantidade de elementos que deseja em sua lista: "))

        if Opcao == 1:
            for i in range(0, Qtd_Num_List):
                Alternativa = input("Escolha um numero ou letra: ")
                array.append(Alternativa)

        if Opcao == 2:
            for i in range(0, Qtd_Num_List):
                if i % 2 == 0:
                    Aleatorio = random.choice(string.ascii_letters)
                else:
                    Aleatorio = random.choice(string.digits)

                array.append(Aleatorio)

        return array
