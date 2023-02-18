Num=int(input("Digite um número: "))
print("Qual o valor de conversão:\n[1] BINARIO\n[2] OCTAL\n[3] HEXADECIMAL")
Option=int(input("Sua opção: "))

if Option == 1:
    print("Valor em binario: ",bin(Num)[2:])
elif Option == 2:
    print("Valor em octal: ",oct(Num)[2:])
elif Option == 3:
    print("Valor em Hexadecimal: ",hex(Num)[2:])
else:
    print("Opção invalida...")