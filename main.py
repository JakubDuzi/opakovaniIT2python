import random

# 1. Proměnná jména
jmeno = "Jan"

# 2. Proměnná příjmení
prijmeni = "Novak"

# 3. Vypsání proměnných
print("Jméno: " + jmeno)
print("Příjmení: " + prijmeni)

# 4. 9. a bonus. Dal jsem je k sobě 
# isdigit kontroluje zda to jsou jenom čísla a vrací True
# Pak už to vlastně funguje jako klasický while cyklus
while True:
    vek_input = input("Zadejte svůj věk: ")
    if vek_input.isdigit():
        vek = int(vek_input)
        print("Děkuji")
        break
    else:
        print("Zadej jen hceločíselnou hodnotu.")

# 5. Vypíše délky jména a příjmění
print ("Délka jména: " + str(len(jmeno)))
print ("Délka příjmení: " + str(len(prijmeni)))

# 6. Proměnná s hodnotou 6
hodnota = 6

# 7. for cyklus s přičítáním čísla 3 pět krát
for i in range(5):
    hodnota += 3

# 8. Vypíše výslednou hodnotu a str konvertuje hodnotu int na string, jinak to nevypíše
print("Výsledná hodnota po 5 cyklech: " + str(hodnota))

# 11. Zde se využáje imporované funkce random a to tím že vygenerujeme pomocí ní náhodné číslo a následně printem vypíšeme
nahodna_hodnota = random.randint(1, 10)
print("Náhodná hodnota od 1 do 10: " + str(nahodna_hodnota))

