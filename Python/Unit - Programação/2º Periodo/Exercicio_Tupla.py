"""
Crie um programa modularizado com uma função que recebe duas
temperaturas, em Celsius ou Farenheint, e informa qual a mais alta.
Caso as temperaturas sejam de escalas diferentes, a função deve fazer
uma conversão para verificar qual a temperatura mais alta.

Fórmulas:

(0 °C × 9/5) + 32 = 32 °F
(32 °F − 32) × 5/9 = 0 °C
"""
Temp1 = ()
Temp2 = ()
print("F - Farenheint | C - Celsius")
Opcao1 = input("Digite Qual o tipo de temperatura: "), \
         float(input("Digite o valor da temperatura: "))
Opcao2 = input("Digite Qual o tipo de temperatura: "), \
         float(input("Digite o valor da temperatura: "))

Temp1 += Opcao1
Temp2 += Opcao2
if Temp1[0] and Temp2[0] == 'C' or Temp1[0] and Temp2[0] == 'F':



if Temp1[0] == 'C' and Temp2[0] == 'F' or Temp1[0] == 'F' and Temp2[0] == 'C':
    if Temp1[0] == "C" and Temp2[0] == "F":
        Conversao = (Temp1[1] * 9 / 5) + 32
        if Conversao > Temp2[1]:
            print(f"{Temp1[1]}°C (ou {Conversao:.2f}°F) é maior que {Temp2[1]}°F")

        elif Conversao < Temp2[1]:
            print(f"{Temp1[1]}°C (ou {Conversao:.2f}°F) é menor que {Temp2[1]}°F")

    elif Temp1[0] == "F" and Temp2[0] == "C":
        Conversao = (Temp1[1] - 32) * 5 / 9
        if Conversao > Temp2[1]:
            print(f"{Temp1[1]}°F (ou {Conversao:.2f}°C) é maior que {Temp2[1]}°C")

        elif Conversao < Temp2[1]:
            print(f"{Temp1[1]}°F (ou {Conversao:.2f}°C) é menor que {Temp2[1]}°C")