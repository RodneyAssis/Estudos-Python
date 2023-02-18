"""Dic = {'One':1, 'Two':2, 'three':3}

print("Mostando Dicionario:")
print(Dic)
# {'One':1, 'Two':2, 'three':3}

print("Deletando uma partição do Dicionario:")
del Dic['One']
print(Dic)
# {'Two':2, 'three':3}

print("Alteração dos elementos do dicionario:")
Dic['three'] = 'may cul'
print(Dic)
# {'Two':2, 'three': 'may cul'}

print("Conferir a quantidade de elementos:")
print(len(Dic)
# 2


print("Retornando nos elementos do dicionario:")
for i in Dic.keys():
    print(Dic[i])
Key_Dicionario = list(Dic.keys())
print(Key_Dicionario)

print("Operadores com dicionarios:")
if 'One' in Dic:
    print("Existe!")
else:
    print("Não Existe!")

print("Outra forma de fazer:")
if Dic.get('One') == 1:
    print("Existe!")
else:
    print("Não existe!")
"""
