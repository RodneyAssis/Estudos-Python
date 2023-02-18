from tkinter import *


def cadastro_medico():
    janela_med = Tk()
    nome = input("Digite o nome do médico")
    print(nome)
    janela_med.mainloop()

janela = Tk()
janela.title("RD INFORMATICA")

janela.wm_geometry("500x300")

texto_titulo = Label(janela, text="Escolha uma das alternativas.")
texto_titulo.grid(column=0, row=0)


botao1 = Button(janela, text="1.Cadastrar médico", command=cadastro_medico)
botao1.grid(column=0, row=1)

janela.mainloop()
