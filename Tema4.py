import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

print("Bine ai venit la Spânzurătoare!")
print("Cuvântul de ghicit este: " + " ".join(progres))
print(f"Încercări rămase: {incercari_ramase}")
print()

while incercari_ramase > 0 and "_" in progres:
    litera = input("Introdu o literă: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Eroare! Introdu o literă validă (o singură literă, fără alte caractere).")
        continue

    if litera in litere_incercate:
        print("Ai mai încercat această literă. Încearcă altceva.")
        continue

    litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
        print(f"Bravo! Litera {litera} se află în cuvânt.")
    else:
        incercari_ramase -= 1
        print(f"Greșit! Litera {litera} nu se află în cuvânt.")

    print("Progres: " + " ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}")
    print()

if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")
