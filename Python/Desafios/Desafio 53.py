Escreva = str(input("Digite algo: ")).replace(" ","")
Reverso ="".join(reversed(Escreva))
if Escreva.lower() == Reverso.lower():
    print("É Polidromo")
    print("O que foi escrito: ",Escreva,"Invertido: ",Reverso)
else:
    print("Não é um Polidromo")
    print("O que foi escrito: ",Escreva,"Invertido: ",Reverso)