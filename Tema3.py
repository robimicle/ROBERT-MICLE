meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

for student in studenti:
    if not comenzi or not tavi:
        break

    comanda_curenta = comenzi.pop(0)
    if comanda_curenta in meniu:
        print(f"{student} a comandat {comanda_curenta}.")
        istoric_comenzi.append(comanda_curenta)
        tavi.pop()
        meniu.remove(comanda_curenta)

comenzi_count = {produs: 0 for produs in ["papanasi", "ceafa", "guias"]}
for comanda in istoric_comenzi:
    comenzi_count[comanda] += 1


print(
    f"S-au comandat {comenzi_count['guias']} guias, {comenzi_count['ceafa']} ceafa, {comenzi_count['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")

print(f"Mai este ceafa: {'ceafa' in meniu}.")
print(f"Mai sunt papanasi: {'papanasi' in meniu}.")
print(f"Mai sunt guias: {'guias' in meniu}.")


total_venit = sum([pret[1] for pret in preturi if pret[0] in istoric_comenzi])
print(f"Cantina a încasat: {total_venit} lei.")

produse_accceptabile = [pret for pret in preturi if pret[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_accceptabile}.")
