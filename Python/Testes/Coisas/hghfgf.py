Voto_Windows = []
Cont_Win = 0
Voto_Linux = []
Cont_Lin = 0
Voto_Mac_OS = []
Cont_Mc = 0
Voto_Outro = []
Cont_Ou = 0
TotalV = 0
cont = 0
while True:

    cont += 1
    print("Pesquisa da enquete: Qual é o melhor Sistema Operacional?")
    nome = str(input('Qual o nome do eleitor? '))
    print('1-Windows \n2-Linux \n3-Mac \n4-Outros')
    alter = int(input('Vote em qual será o melhor sistema operacional: '))
    print()
    if alter == 0:
        break
    if alter < 0 or alter > 4:
        print('Não possui essa opção.')
    if alter == 1:
        Voto_Windows.append(nome)
        Cont_Win += 1
        TotalV += 1
    if alter == 2:
        Voto_Linux.append(nome)
        Cont_Lin += 1
        TotalV += 1
    if alter == 3:
        Voto_Mac_OS.append(nome)
        Cont_Mc += 1
        TotalV += 1
    if alter == 4:
        Voto_Outro.append(nome)
        Cont_Ou += 1
        TotalV += 1

win = Cont_Win/TotalV
Pcwin = win*100
lin = Cont_Lin/TotalV
Pclin = lin*100
mc = Cont_Mc/TotalV
Pcmc = mc*100
outros = Cont_Ou/TotalV
Pcoutros = outros*100

print('Total de votos foi {}'.format(TotalV))
print('Votos dos Sistemas Operacionais: ')
print('Windows: {} \nLinux: {} \nMac_OS: {} \nOutros: {}'.format(Cont_Win,Cont_Lin,Cont_Mc,Cont_Ou))
print('Porcent.(%):')
print('Porcent. Windows: {:.1f}%'.format(Pcwin))
print('Porcent. Linux: {:.1f}%'.format(Pclin))
print('Porcent. Mac: {:.1f}%'.format(Pcmc))
print('Porcent. opção Outros: {:.1f}%'.format(Pcoutros))
if Cont_Win > Cont_Lin and Cont_Win > Cont_Mc and Cont_Win > Cont_Ou:
    print('Vencedor: Windows.')
elif Cont_Lin > Cont_Win and Cont_Lin > Cont_Mc and Cont_Lin > Cont_Ou:
    print('Vencedor: Linux.')
elif Cont_Mc > Cont_Win and Cont_Mc > Cont_Lin and Cont_Mc > Cont_Ou:
    print('Vencedor: Mac.')
elif Cont_Ou > Cont_Win and Cont_Ou > Cont_Lin and Cont_Ou > Cont_Mc:
    print('Vencedor: Outro.')
else:
    print('Sem vencedor')
