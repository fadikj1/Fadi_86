list = []
maxNummbelInList = int(input("skris ett antal sifra för innehåller:  "))

for i in range (0, maxNummbelInList):
    nr = int(input("matta in en siffra:  "))
    list.append(nr)


print("Minsta siffran är: ", min(list))

print("Största siffran är: ", max(list))
