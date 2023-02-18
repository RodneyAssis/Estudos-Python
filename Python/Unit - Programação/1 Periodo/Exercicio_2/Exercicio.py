QtdM = 0
IdadeM = 0
QtdF = 0
IdadeF = 0
Cont = 0
Maior_idade = 18
QtdId18 = 0
while True:
    Matricula=int(input("Digite o seu número de matricula: "))
    if Matricula < 0:
        break

    Sexo=str(input("Digite seu Sexo (M ou F): ")).upper()
    Idade=int(input("Digite a idade: "))
    print("")
    Cont = Cont + 1

    if Sexo == "M":
        QtdM = QtdM + 1
        IdadeM = IdadeM + Idade
    else:
        QtdF = QtdF + 1
        IdadeF = IdadeF + Idade

    if Idade >= 18:
        QtdId18 = QtdId18 + 1


print(f"Quantidade de alunos: {Cont}")
print(f"Quantidade de alunos de Sexo Masculino é: {QtdM}\nJá as do Sexo Feminino é: {QtdF}")
print("")
if (QtdM > 0) and (QtdF > 0):
    print(f"Média da idades dos homens: {IdadeM/QtdM}")
    print(f"Média da idades das mulher: {IdadeF/QtdF}")
elif (QtdM > 0) and (QtdF == 0):
    print(f"Média da idades dos homens: {IdadeM / QtdM}")
else:
    print(f"Média da idades das mulher: {IdadeF / QtdF}")

print(f"Quantidade de alunos de 18 anos pra cima: {QtdId18}")