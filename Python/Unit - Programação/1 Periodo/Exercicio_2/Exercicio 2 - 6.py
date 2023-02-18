while(True):
    n = int(input('Informe n:'))
    if (n <= 5000):
        break
lin = 1
for lin in range(1,n+1):
    for col in range(1, lin+1):
        print(f'{col:02d}', end = ' ')
    print()

print('\nFim')
