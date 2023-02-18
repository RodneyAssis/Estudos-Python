Qtd_Cidades=int(input("Digite a quantidade de cidades: "))
cont=0
Total_Carros=0
Total_Motocicletas=0
Total_Acidentes=0
Nome_Cidades=[]
Num_Carros_Passeio1=[]
Num_Motocicletas1=[]
Num_Acidentes1=[]
while True:
    if cont == Qtd_Cidades:
        break
    Nome_Cidades.append(input("Digite o nome da cidade: "))
    Num_Carros_Passeio=int(input("Digite a quantidade de carros de passeio: "))
    Num_Carros_Passeio1.append(Num_Carros_Passeio)
    Total_Carros=Total_Carros+Num_Carros_Passeio

    Num_Motocicletas=(int(input("Digite a quantidade de motocicletas: ")))
    Num_Motocicletas1.append(Num_Motocicletas)
    Total_Motocicletas= Total_Motocicletas + Num_Motocicletas

    Num_Acidentes=int(input("Quantidade de acidentes em 2019: "))
    Num_Acidentes1.append(Num_Acidentes)
    Total_Acidentes=Total_Acidentes + Num_Acidentes
    print("")
    cont = cont + 1

print(f"Numero de cidades: {Qtd_Cidades}")
Media_Carros = Total_Carros/Qtd_Cidades
print(f"Media de Carros: {Media_Carros}")
Media_Motocicletas = Total_Motocicletas/Qtd_Cidades
print(f"Média de Motocicletas: {Media_Motocicletas}")
Media_Acidentes = Total_Acidentes/Qtd_Cidades
print(f"Média de Acidentes: {Media_Acidentes}")
print("")

Menor_Acidentes=[]
Maior_Acidentes=[]

Menor_Acidentes.append(Nome_Cidades[Num_Acidentes1.index(min(Num_Acidentes1))])
Menor_Acidentes.append(min(Num_Acidentes1))
print(f"O menor número de acidentes aconteceu na Cidade {Menor_Acidentes[0]}, com aproximadamente"
      f" {Menor_Acidentes[1]} Acidentes""")

Maior_Acidentes.append(Nome_Cidades[Num_Acidentes1.index(max(Num_Acidentes1))])
Maior_Acidentes.append(max(Num_Acidentes1))
print(f"O maior número de acidentes aconteceu na Cidade {Maior_Acidentes[0]}, com aproximadamente"
      f" {Maior_Acidentes[1]} Acidentes""")