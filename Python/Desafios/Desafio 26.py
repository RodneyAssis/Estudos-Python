text=str(input("Digite um texto: ")).strip().upper()

print("A letra 'a' é encontrada: ",text.count("A"))
print("Aparece na primeira vez: ",text.upper().find("A")+1)
print("Aparece na ultima vez: ",text.upper().rfind("A")+1)