#Wczytywanie liczby i parametrów procesów z pliku
procesy = []
with open("dane_procesy.txt", "r", encoding="utf-8") as plik:
    linie = [linia.strip() for linia in plik if linia.strip()]
    liczba_procesow = int(linie[0])
    for i in range(1, liczba_procesow + 1):
        czas_przybycia, czas_wykonania = map(int, linie[i].split())
        procesy.append({
            'proces_id': f'P{i}',
            'czas_przybycia': czas_przybycia,
            'czas_wykonania': czas_wykonania
        })

# Sortowanie według czasu wykonania
procesy.sort(key=lambda p: p["czas_wykonania"])

# Obliczanie czasu wyjścia, realizacji i oczekiwania
czas_początkowy = 0
for p in procesy:
    if czas_początkowy < p['czas_przybycia']:
        czas_początkowy = p['czas_przybycia']
    p['czas_wyjscia'] = czas_początkowy + p['czas_wykonania']
    czas_początkowy = p['czas_wyjscia']
    p['realizacja'] = p['czas_wyjscia'] - p['czas_przybycia']
    p['oczekiwanie'] = p['realizacja'] - p['czas_wykonania']

# Obliczanie średniego czasu oczekiwania
sredni_czas_oczekiwania = sum(p['oczekiwanie'] for p in procesy) / liczba_procesow

# Wyświetlanie wyników
print("\n{:<8} {:<15} {:<15} {:<13} {:<18} {:<18}".format(
    "Proces", "Czas przybycia", "Czas wykonania", "Czas wyjścia", "Czas realizacji", "Czas oczekiwania"))

for p in procesy:
    print("{:<8} {:<15} {:<15} {:<13} {:<18} {:<18}".format(
        p['proces_id'],
        p['czas_przybycia'],
        p['czas_wykonania'],
        p['czas_wyjscia'],
        p['realizacja'],
        p['oczekiwanie']
    ))


print(f"\nŚredni czas oczekiwania: {sredni_czas_oczekiwania:.2f}")

#Zapisywanie wyników do pliku

with open("wyniki_sjf.txt", "w", encoding="utf-8") as wynik_plik:
    wynik_plik.write("SJF – Wyniki:\n")
    wynik_plik.write("{:<8} {:<15} {:<15} {:<13} {:<18} {:<18}\n".format(
        "Proces", "Czas przybycia", "Czas wykonania", "Czas wyjścia", "Czas realizacji", "Czas oczekiwania"))

    for p in procesy:
        wynik_plik.write("{:<8} {:<15} {:<15} {:<13} {:<18} {:<18}\n".format(
            p['proces_id'], p['czas_przybycia'], p['czas_wykonania'],
            p['czas_wyjscia'], p['realizacja'], p['oczekiwanie']
        ))

    wynik_plik.write(f"\nŚredni czas oczekiwania: {sredni_czas_oczekiwania:.2f}\n")



