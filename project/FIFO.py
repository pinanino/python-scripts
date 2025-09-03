from collections import deque

#Tworzymy zmienne, gdzie mamy ilosc zaladowanych teraz stron, kolejkę i błędy
def bledy_strony_fifo(strony, ilosc, pojemnosc):
    pamiec = set()
    kolejka = deque()
    bledy = 0

#Sprawdzamy czy strona znajduje się w pamięci
#Szukamy tej, która jest najstarsza i ją usuwamy, a następnie dodajemy nową do pamięci i kolejki
    for strona in strony:
        if strona not in pamiec:
            if len(pamiec) >= pojemnosc:
                usunieta = kolejka.popleft()
                pamiec.remove(usunieta)

            pamiec.add(strona)
            kolejka.append(strona)
            bledy += 1

    return bledy

#Wczytujemy dane z pliku wewnątrz kodu
with open("dane.txt", "r", encoding="utf-8") as plik:
    linie = [linia.strip() for linia in plik if linia.strip() != '']

#Otwieramy plik do zapisu i zapisujemy w nim wyniki
with open("wyniki_fifo.txt", "w", encoding="utf-8") as wynik_plik:
    for i in range(0, len(linie), 2):
        strony = list(map(int, linie[i].split()))
        pojemnosc = int(linie[i + 1])
        ilosc = len(strony)

        wynik = bledy_strony_fifo(strony, ilosc, pojemnosc)

        wynik_plik.write(f"\nFIFO - Zestaw {i // 2 + 1}:\n")
        wynik_plik.write(f"Strony:     {strony}\n")
        wynik_plik.write(f"Pojemność:  {pojemnosc}\n")
        wynik_plik.write(f"Błędy:      {wynik}\n")
