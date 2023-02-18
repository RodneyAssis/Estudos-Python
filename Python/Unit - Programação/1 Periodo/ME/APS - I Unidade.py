# APS-UNIT                                                                                   Data: 05/04/2020
# Curso: Ciencias da Computação
# Turma: Fundamentos da Programação
# Profº.: Virgilio Antonio N C de Faro
# Alunos: Rodney Assis Matos Furtado/ Yuri Rezende Santos

Numero_carro1 = []
Nome_piloto = []
Tempo = []
Tempo_punicao = []

Quantidade_carro = 0
Tempo_Max = 0
Cont=0

Primeiro = []
Segundo = []

while True:
    Cont=Cont+1
    Numero_carro=(int(input(f"Número do {Cont}º carro: ")))
    if Numero_carro < 0:
        print("")
        break
    Quantidade_carro = Quantidade_carro + 1
    Numero_carro1.append(Numero_carro)
    Nome_piloto.append(str(input(f"Nome do {Cont}º piloto: ")))
    Tempo_corrida=(float(input("Tempo da Corrida: ")))
    Tempo.append(Tempo_corrida)
    Tempo_Max = Tempo_Max + Tempo_corrida
    Punicao = (int(input("Número de punições: ")))
    Punicao1 = Tempo_corrida+(Tempo_corrida*(Punicao*0.05))
    Tempo_punicao.append(Punicao1)
    print("")
print("Números de carros participando:",Quantidade_carro)
print("Tempo total da corrida: {:.0f}segs".format(Tempo_Max))
Tempo_Medio = (Tempo_Max/Quantidade_carro)
print("Tempo Médio: {:.0f}hrs:{:.0f}mins:{:.0f}segs".format((Tempo_Medio//3600),(Tempo_Medio//60),(Tempo_Medio%60)))
print("")

Primeiro.append(Nome_piloto[Tempo_punicao.index(min(Tempo_punicao))])
Primeiro.append(Numero_carro1[Tempo_punicao.index(min(Tempo_punicao))])
Primeiro.append(min(Tempo_punicao))

Tempo_punicao2 = sorted(Tempo_punicao)

Seg = Tempo_punicao.index(Tempo_punicao2[1])
Segundo.append(Nome_piloto[Seg])
Segundo.append(Numero_carro1[Seg])
Segundo.append(Tempo_punicao2[1])

print(f"O Primeiro colocado foi o piloto {Primeiro[0]} com o carro nº:{Primeiro[1]} com o tempo de {Primeiro[2]}segs")
print(f"O Segundo colocado foi o piloto {Segundo[0]} com o carro nº:{Segundo[1]} com o tempo de {Segundo[2]}segs")
