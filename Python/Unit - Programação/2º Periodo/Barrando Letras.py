import string
Alphabet = list(string.ascii_letters) + list(string.punctuation)
cpf = ''
Letra = ''
while True:
    cpf = str(input(f'\nInforme seu CPF: '))
    for i in cpf:
        if i in Alphabet:
            Letra = i
    if Letra in Alphabet:
        print("Possui letra")
    if len(str(cpf)) != 11:
        print(f'\n\033[0;31mInforme somente os 11 números do CPF!\033[0;00m')
