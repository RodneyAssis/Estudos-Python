"""


"""


cd_atendimento = 0
especialistas = ["Clinico Geral", "Nutricionista", "Fonoaudioterapeuta",
                 "Fisioterapeuta", "Odontologia"]
valor_consulta = [250, 150, 200, 150, 200]
total_especialistas = [0, 0, 0, 0, 0]
total_client_59_convenio = 0
total_atend = 0
total_fisio = 0
total_arrecadado = 0
while True:
    print(f"Atendimento num: {total_atend+1:03}")
    cpf = input("Informar cpf do cliente: ")
    if cpf == "-1":
        break
    nome = input("Informar nome do cliente: ")
    idade = int(input("Informar idade do cliente: "))
    convenio = input("\nSIM - S | NÃO - N\n"
                     "Cliente possui convenio: ").upper()
    opcao = int(input("CONSULTAS:\n\n1- Clinico Geral\n2- Nutricionista\n3- Fonoaudiologo\n"
                      "4- Fisioterapeuta\n5- Odontologia\n\nInforme a consulta do cliente: "))
    if convenio == "S":
        if idade > 59:
            total_client_59_convenio += 1
        print("Cliente com convenio possuem desconto de 75%")
        if opcao == 1:
            total_especialistas[0] += 1
            print(f"Valor bruto da  consulta com o {especialistas[0]} ficará no valor de: R$ {valor_consulta[0]}")
            desconto = valor_consulta[0] - (valor_consulta[0] * 0.75)
            print(f"O valor com desconto: R$ {desconto:.2f}")
            total_arrecadado += desconto
        elif opcao == 2:
            total_especialistas[1] += 1
            print(f"Valor bruto da  consulta com o {especialistas[1]} ficará no valor de: R$ {valor_consulta[1]}")
            desconto = valor_consulta[1] - (valor_consulta[1] * 0.75)
            print(f"O valor com desconto: R$ {desconto:.2f}")
            total_arrecadado += desconto
        elif opcao == 3:
            total_especialistas[2] += 1
            print(f"Valor bruto da  consulta com o {especialistas[2]} ficará no valor de: R$ {valor_consulta[2]}")
            desconto = valor_consulta[2] - (valor_consulta[2] * 0.75)
            print(f"O valor com desconto: R$ {desconto:.2f}")
            total_arrecadado += desconto
        elif opcao == 4:
            total_especialistas[3] += 1
            print(f"Valor bruto da  consulta com o {especialistas[3]} ficará no valor de: R$ {valor_consulta[3]}")
            desconto = valor_consulta[3] - (valor_consulta[3] * 0.75)
            print(f"O valor com desconto: R$ {desconto:.2f}")
            total_arrecadado += desconto
            total_fisio += 1
        elif opcao == 5:
            total_especialistas[4] += 1
            print(f"Valor bruto da consulta com o {especialistas[4]} ficará no valor de: R$ {valor_consulta[4]}")
            desconto = valor_consulta[4] - (valor_consulta[4] * 0.75)
            print(f"O valor com desconto: R$ {desconto:.2f}")
            total_arrecadado += desconto
    elif convenio == "N":
        if opcao == 1:
            print(f"Valor da consulta com o {especialistas[0]} ficará no valor de: R$ {valor_consulta[0]:.2f}")
            total_especialistas[0] += 1
            total_arrecadado += valor_consulta[0]
        elif opcao == 2:
            print(f"Valor da consulta com o {especialistas[1]} ficará no valor de: R$ {valor_consulta[1]:.2f}")
            total_especialistas[1] += 1
            total_arrecadado += valor_consulta[1]
        elif opcao == 3:
            print(f"Valor da consulta com o {especialistas[2]} ficará no valor de: R$ {valor_consulta[2]:.2f}")
            total_especialistas[2] += 1
            total_arrecadado += valor_consulta[2]
        elif opcao == 4:
            print(f"Valor da consulta com o {especialistas[3]} ficará no valor de: R$ {valor_consulta[3]:.2f}")
            total_especialistas[3] += 1
            total_arrecadado += valor_consulta[3]
            total_fisio += 1
        elif opcao == 5:
            print(f"Valor da consulta com o {especialistas[4]} ficará no valor de: R$ {valor_consulta[4]:.2f}")
            total_especialistas[4] += 1
            total_arrecadado += valor_consulta[4]
    total_atend += 1
    print("")
print("\n"*30)
print("-*-*-*-*-*-RELATORIO DO FINAL DE EXPEDIENTE-*-*-*-*-*-\n")
print("-=-"*30)
# RESPOSTA LETRA A
print("RELAÇÃO DOS ESPECIALISTAS:")
for i in range(0, len(total_especialistas)):
    print(f"{especialistas[i]}: {total_especialistas[i]} pacientes registrados")
print("-=-"*30)
print(f"Total de atendimentos realizados: {total_atend:03}")
print("-=-"*30)
# RESPOSTA LETRA B
print(f"Clientes que possuem acima de 59 anos + convenio: {total_client_59_convenio}")
print("-=-"*30)
# RESPOSTA LETRA C
print(f"Total de clientes que realizaram consulta com o fisioterapeuta: {total_fisio}")
porcent_fisio = (total_fisio*100)/total_atend
print(f"Porcentual de clientes que realizaram procedimento com o fisioterapeuta: {porcent_fisio}%")
print("-=-"*30)
# RESPOSTA LETRA D
print(f"Total Arrecadados no final do expediente: R${total_arrecadado}")
print("-=-"*30)