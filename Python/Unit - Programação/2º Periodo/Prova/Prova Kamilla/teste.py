class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def Envelhecer(self):
        if self.idade < 21:
            self.idade += 1
            self.altura += 0.5
        else:
            self.idade += 1

    def Engordar(self):
        self.peso += 2

    def Emagrecer(self):
        self.peso -= 2

    def Crescer(self):
        self.altura += 1

    def Mostrar_Dados(self):
        return f'\nNome: {self.nome} \nIdade: {self.idade} ' \
               f'\nPeso: {self.peso} \nAltura: {self.altura}'


nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

info = Pessoa(nome, idade, peso, altura)
print(info)
while True:
    print('Olá', nome)
    print(info.Mostrar_Dados())
    op = int(input('\n[1] Envelhecer \n[2] Engordar'
                   '\n[3] Emagrecer  \n[4] Crescer'
                   ' \n\nDigite a opção: '))
    if op == 1:
        info.Envelhecer()
    if op == 2:
        info.Engordar()
    if op == 3:
        info.Emagrecer()
    if op == 4:
        info.Crescer()
