lin = 1
while True:
    n = int(input("Digite um valor a n: "))
    if (n<=100):
        break

lin = 1

for lin in range(1,n+1):
    for col in range(1,lin+1):
        print(col , end = " ")
    print("")
print("\nFim")