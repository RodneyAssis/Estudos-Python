Cidade=str(input("Digite o nome de sua cidade: ")).strip()
Cidade.upper().find("SANTO")

if (Cidade.upper().find("SANTO") == -1) or (Cidade.upper().find("SANTO") >= 1):
    print("Não começa com Santo")
else:
    print("Começa com Santo,",Cidade)

#Solução Unica
#print("Começa com Santo: {}".format(Cidade.upper()[:5] == "SANTO"))