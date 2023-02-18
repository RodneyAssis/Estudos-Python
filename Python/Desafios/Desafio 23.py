valor=int(input("Digite um valor entre 0000 e 9999: "))
u= valor % 10
d= valor // 10 % 10
c= valor // 100 % 10
m= valor // 1000 % 10
print("Unidade: ",u)
print("Desena: ",d)
print("Centena: ",c)
print("Milhar: ",m)
