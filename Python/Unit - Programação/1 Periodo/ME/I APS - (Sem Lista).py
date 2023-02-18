# APS-UNIT                                                                                   Data: 05/04/2020
# Curso: Ciencias da Computação
# Turma: Fundamentos da Programação
# Profº.: Virgilio Antonio N C de Faro
# Alunos: Rodney Assis Matos Furtado/ Yuri Rezende Santos
Quantidade_carro = 0
Tempo_Max = 0
Cont=0

Primeiro_Lugar = 99999999999
Nome_Primeiro = ""
N_Carro = ""

Segundo_Lugar = 0
Nome_Segundo = ""
N_Carro2 = ""

while True:
    Cont=Cont+1
    Numero_carro= int(input(f"Número do {Cont}º carro: "))
    if Numero_carro < 0:
        print("")
        break
    Quantidade_carro = Quantidade_carro + 1
    Nome_piloto = (str(input(f"Nome do {Cont}º piloto: ")))
    Tempo_corrida=(float(input("Tempo da Corrida: ")))
    Tempo_Max = Tempo_Max + Tempo_corrida
    Punicao = (int(input("Número de punições: ")))
    Tempo_Bruto = Tempo_corrida+(Tempo_corrida*(Punicao*0.05))
    if Tempo_Bruto < Primeiro_Lugar:
        N_Carro = Numero_carro
        Nome_Primeiro = Nome_piloto
        Primeiro_Lugar = Tempo_Bruto
    if Tempo_Bruto > Primeiro_Lugar:
        N_Carro2 = Numero_carro
        Nome_Segundo = Nome_piloto
        Segundo_Lugar = Tempo_Bruto
    print("")

print("Números de carros participando:",Quantidade_carro)
print("Tempo total da corrida: {:.0f}segs".format(Tempo_Max))
Tempo_Medio = (Tempo_Max/Quantidade_carro)
print("Tempo Médio: {:.0f}hrs:{:.0f}mins:{:.0f}segs".format((Tempo_Medio//3600),(Tempo_Medio//60),(Tempo_Medio%60)))
print("")

print(f"Primeiro Lugar foi o carro nº{N_Carro} do piloto {Nome_Primeiro} com tempo de: {Primeiro_Lugar}segs")
print(f"Segundo Lugar foi o carro nº{N_Carro2} do piloto {Nome_Segundo} com tempo de: {Segundo_Lugar}segs")