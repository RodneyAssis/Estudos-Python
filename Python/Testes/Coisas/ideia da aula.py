while True:
    N=int(input("Digite um valor"))
    P=int(input("Digite um valor"))
    i=1
    fatN=1
    fatP=1
    if N > P:
        break
for i in range(1,N+1):
    fatN=fatN*i
print(f"Valor N:{fatN}")

for i in range(1,P+1):
    fatP = fatP * i
print(f"Valor P:{fatP}")

if N > P:
    print(fatN-fatP)
    s = (fatN / (fatP * (fatN-fatP)))*fatP
    print(s)


