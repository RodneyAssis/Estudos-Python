a=1

while a <= 100:
    print(a, end=" ")
    a = 1 + a
    print(a)

    if (a % 7 == 0):
        print("Multiplo de 7:", a)
print("-------------")
print("Fora do while")