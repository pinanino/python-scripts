#Tworzymy potrzebne zmienne
def bledy_strony_lru(strony, ilosc, pojemnosc):
    pamiec = set()
    indeksy = {}
    bledy = 0

#Przechodzimy przez każdą stronę
    for i in range(ilosc):
        strona = strony[i]

#Sprawdzamy czy strona znajduje się w pamięci
#Szukamy tej, która najdłużej nie była używana i ją usuwamy, a następnie aktualizujemy indeks
        if strona not in pamiec:
            if len(pamiec) >= pojemnosc:
                lru = min(pamiec, key=lambda s: indeksy[s])
                pamiec.remove(lru)

            pamiec.add(strona)
            bledy += 1

        indeksy[strona] = i

    return bledy

#Wczytujemy dane z pliku wewnątrz kodu
with open("dane.txt", "r") as plik:
    linie = [linia.strip() for linia in plik if linia.strip() != '']

#Otwieramy plik do zapisu i zapisujemy w nim wyniki
with open("wyniki_lru.txt", "w", encoding="utf-8") as wynik_plik:
    for i in range(0, len(linie), 2):
        strony = list(map(int, linie[i].split()))
        pojemnosc = int(linie[i + 1])
        ilosc = len(strony)
        wynik = bledy_strony_lru(strony, ilosc, pojemnosc)


        wynik_plik.write(f"\nLRU – Zestaw {i // 2 + 1}:\n")
        wynik_plik.write(f"Strony:     {strony}\n")
        wynik_plik.write(f"Pojemność:  {pojemnosc}\n")
        wynik_plik.write(f"Błędy:      {wynik}\n")
