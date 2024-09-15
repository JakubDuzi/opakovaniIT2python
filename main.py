import random

# 1.
jmeno = "Jan"

# 2.
prijmeni = "Novak"

# 3.
print("Jméno: " + jmeno)
print("Příjmení: " + prijmeni)

# 4. 9. a bonus. Dal jsem je k sobě
while True:
    vek_input = input("Zadejte svůj věk: ")
    if vek_input.isdigit():
        vek = int(vek_input)
        print("Děkuji")
        break
    else:
        print("Zadej jen hceločíselnou hodnotu.")

# 5.
print ("Délka jména: " + str(len(jmeno)))
print ("Délka příjmení: " + str(len(prijmeni)))

# 6.
hodnota = 6

# 7.
for i in range(5):
    hodnota += 3

# 8.
print("Výsledná hodnota po 5 cyklech: " + str(hodnota))

# 11. 
nahodna_hodnota = random.randint(1, 10)
print("Náhodná hodnota od 1 do 10: " + str(nahodna_hodnota))

