Peso = float(input("Digite seu peso: "))
Altura = float(input("Digite sua altura: "))

IMC = Peso/(Altura**2)
print(f"Seu IMC é: {IMC:.0f}")

if IMC < 18.5:
    print("Você está abaixo de peso ideal")
elif IMC < 25 and IMC >=18.5:
    print("Você está no peso ideal")
elif IMC < 30 and IMC >= 25:
    print("Você Está um pouco acima do peso")
elif IMC < 40 and IMC >= 30:
    print("Você está em fase de obesidade")
else:
    print("Você está fase de Obesidade morbida.")