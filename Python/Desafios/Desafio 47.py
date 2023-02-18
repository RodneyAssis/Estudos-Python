print("Os números entre 1 à 50 apenas...")
for i in range(1,50+1):
    par = i%2
    if par == 0:
        print(end=f"-|{i}|")
print()
print("são pares.")