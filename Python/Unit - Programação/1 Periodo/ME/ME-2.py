# ME.2-UNIT                                                                                   Data: 05/04/2020
# Curso: Ciencias da Computação
# Turma: Fundamentos da Programação
# Profº.: Virgilio Antonio N C de Faro
# Alunos: Rodney Assis Matos Furtado/ Yuri Rezende Santos/ José Cláudio Sousa/
#         Lucas Ribeiro Pereira/ Iago Guimarães/ Lucas Gabriel Souza

from random import randint
from time import sleep
from operator import itemgetter

atirador1 = (input("Nome do atirador: ")), (str(input("Sexo [M] ou [F]: ")))
atirador2 = (input("Nome do atirador: ")), (str(input("Sexo [M] ou [F]: ")))
atirador3 = (input("Nome do atirador: ")), (str(input("Sexo [M] ou [F]: ")))

Atiradores= atirador1 + atirador2 + atirador3 #Soma de todos atiradores de Sexo Masculino.
print("")
atirador = {atirador1: randint(1, 40)/10,
            atirador2: randint(1, 40)/10,
            atirador3: randint(1, 40)/10}
Total_Media = 0
Ranking = []
print ("Atirem")
print ('')
for k, v in atirador.items():
    print(f'{k} realizou o tiro {v} centimetros.')
    sleep(2)
Ranking = sorted(atirador.items(), key=itemgetter(1), reverse=False)
print("")
for i, v in enumerate(Ranking):
    print(f'  {i+1}º lugar:{v[0]} distancia: {v[1]}cm do alvo ') # RESPOSTA DA B) E SEGUNDA B)
    Soma = v[1]
    sleep(1)
    Total_Media = Total_Media + Soma

print("Numero de atiradores do sexo masculino:",Atiradores.count("M")) # RESPOSTA DA C)
print("")
print("Média da distância:",Total_Media/3) # RESPOSTA DA D)
