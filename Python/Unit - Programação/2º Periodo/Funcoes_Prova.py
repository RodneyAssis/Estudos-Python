def Clientes_Status(Dicionario):
    with open("Registro_Atividade.txt") as Registra:
        for Linha in Registra:
            (CPF, Status) = Linha.split()
            Dicionario[CPF] = Status


def Clientes_Reservas(Dicionario):  # Terminar depois #imcompleto
    with open("Registro_Reserva.txt") as Reserva:
        for Linha in Reserva:
            (CPF, Reserva) = Linha.split()
            Dicionario[CPF] = Reserva
