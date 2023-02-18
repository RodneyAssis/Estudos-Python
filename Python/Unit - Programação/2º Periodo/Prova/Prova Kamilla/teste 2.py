

'''
Imoveis_Cadastrados = {'Codigo': [123, 321], 'CPF_PROP': [], 'Tipo': [],
                       'Endereço': [], 'Valor_Aluguel': [],
                       'Status_Aluguel': [300, 300]}



A = Imoveis_Cadastrados['Codigo'].index(321)
Imoveis_Cadastrados['Status_Aluguel'][A] += Imoveis_Cadastrados['Status_Aluguel'][A]'''
# print(Imoveis_Cadastrados['Status_Aluguel'][A])
Imoveis_Cadastrados = {'Codigo': [321], 'CPF_PROP': [], 'Tipo': [], 'Endereço': [], 'Valor_Aluguel': [],
                       'Status': [], 'Data_inicio': [56354, 'teste'], 'Data_f': []}

A = Imoveis_Cadastrados['Codigo'].index(321)
print(A)
Imoveis_Cadastrados['Data_inicio'][A] = 50
Imoveis_Cadastrados['Data_inicio'] += [40]
print(Imoveis_Cadastrados['Data_inicio'])
