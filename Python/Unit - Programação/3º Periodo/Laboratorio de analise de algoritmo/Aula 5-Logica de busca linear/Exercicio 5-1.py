import Funcao_5_1q

"""
1. Criar uma aplicação, na qual o usuário inicialmente informa um conjunto de dados (pode
ser string ou numérico). Em seguida, o usuário informa um item a ser buscado no conjunto
de dados já informado.
A solução deve ser implementada utilizando os conceitos de Busca Linear/Sequencial
"""
Lista = []

Funcao_5_1q.Escolha_Usuario(Lista)

print(f"Lista produzida: {Lista}")

Procura = input("Digite o numero que deseja buscar na lista: ")

for i in range(0,len(Lista)):
    if Procura not in Lista[i]:
        print(f"O caractere '{Procura}' não esta na posição {Lista.index(Lista[i])} da lista.")
    elif Procura in Lista[i]:
        print(f"Elemento '{Procura}', Encontrasse na posição {Lista.index(Lista[i])} lista.")
        break
    else:
        print("Elemento não encontrado.")