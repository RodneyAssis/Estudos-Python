import PySimpleGUI as sg
import pandas as pd
# Layout da interface grafica
layout = [
    [sg.Text("Nome: ", size=(5, 1)), sg.Input(key='Nome')],
    [sg.Text("Idade: ", size=(5, 1)), sg.Input(key='Idade')],
    [sg.Text("CPF: ", size=(5, 1)), sg.Input(key='CPF')],
    [sg.Button("Enviar"), sg.Button("Sair")],
    [sg.Output(size=(65, 20))]
]

# Inicio da pagina;
Janela = sg.Window('Dados.exe', layout)
ListaNome = []
ListaIdade = []
ListaCPF = []


dados = {'Nome': ListaNome,
         'Idade': ListaIdade,
         'CPF': ListaCPF}

# Condições
Cont = 0
while True:
    event, value = Janela.read()
    try:

        if event == 'Sair' or event == sg.WINDOW_CLOSED:
            break
        elif not value['Idade'].isnumeric() or not value['CPF'].isnumeric():
            sg.popup_ok("Caractere Invalido!\n Tente Novamente.")
        elif value['Nome'] == '' or value['Idade'] == '' or value['CPF'] == '':
            sg.popup_ok("Caractere Invalido!\n Tente Novamente.")
        elif value['CPF'] in ListaCPF:
            sg.popup_ok("Este CPF já se encontra em nosso bando de dados.")

        else:
            if Cont == 0:
                print("Nome\t\t\t\t\tIdade\tCPF")
                for i in range(len(ListaCPF)):
                    print(f"{ListaNome[i].title()}\t\t\t\t\t{ListaIdade[i]}\t{ListaCPF[i]}")
            ListaNome.append(value['Nome'])
            ListaIdade.append(value['Idade'])
            ListaCPF.append(value['CPF'])
            DF = pd.DataFrame(dados)
            print(f"{ListaNome[Cont].title()}\t\t\t\t\t{ListaIdade[Cont]}\t{ListaCPF[Cont]}")
            Cont += 1
    except TypeError or IndexError:
        pass
