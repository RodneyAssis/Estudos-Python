nome=str(input("Digite seu nome: ")).strip()
nome.upper().find("SILVA")

if nome.upper().find("SILVA") >= 0:
    print("Seu nome tem Silva, ",nome)
else:
    print("Seu nome não tem Silva,",nome)

