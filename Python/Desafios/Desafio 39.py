Nome=input("Digite seu nome: ")
Idade=int(input("Digite sua idade: "))

Idade_Alist= Idade - 18

if Idade < 18:
    print(f"{Nome}, você tem {Idade} ainda é muito novo"
          f" para se alistar no serviço militar, tente daqui à {Idade_Alist*(-1)} anos")

elif Idade == 18:
    print(f"{Nome}, você tem idade para se alistar no serviço militar!!")

else:
    print(f"Você já passou do prazo de alistamente já faz {Idade_Alist*(1)} anos")
