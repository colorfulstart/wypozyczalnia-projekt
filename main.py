from jednostki import *
from ludzie import *
from wypozyczalnia import *
from datetime import date, timedelta

# TESTOWANIE
W1 = Wypozyczalnia("1", "Wrocław")
#print(w1.gdzie())
#print(w1.ile_lodek())

#jed1 = jednostka("S1-AB12", "opel", "insygnia", 400, 2003, 5)


#dodani Pracownik
p1 = Pracownik(1, "Tomasz", "Janusz")
p2 = Pracownik(2, "Mateusz", "Rabiega")
p3 = Pracownik(3, "Kamil", "Pajak")
p4 = Pracownik(4, "Marta", "Palma")
W1.dodaj_pracownika(p1)
W1.dodaj_pracownika(p2)
W1.dodaj_pracownika(p3)
W1.dodaj_pracownika(p4)


#cena_za_dobe, rok_produkcji, liczba_pasazerow, liczba_drzwi, moc_silnika, spalanie, skrzynia_biegow
auto1 = Samochod("S1-AB11", "Volkswagen", "Touran", 500, 2014, 7, 5, 140, 5, "manual")
auto2 = Samochod("S2-AB11", "Suziki", "Ignis", 350, 2009, 5, 5, 90, 4.5, "manual")
auto3 = Samochod("S3-AB11", "Toyota", "Aygo", 400, 2016, 5, 5, 110, 6, "manual")
auto4 = Samochod("S3-AB12", "Toyota", "Aygo", 400, 2016, 5, 5, 110, 6, "automat")
auto5 = Samochod("S4-AB11", "Opel", "Insygnia", 470, 2011, 5, 5, 120, 7, "manual")
auto6 = Samochod("S5-AB11", "Toyota", "Aygo", 400, 2016, 5, 5, 110, 6, "manual")

W1.dodaj_auto(auto1)
W1.dodaj_auto(auto2)
W1.dodaj_auto(auto3)
W1.dodaj_auto(auto4)
W1.dodaj_auto(auto5)
W1.dodaj_auto(auto6)

lodka1 = Zaglowka("LJ1-AB11", "Antila", "27", 360, 2012, 8, 8.4, 38, "plaski ster", "tak", 3)
lodka2 = Zaglowka("LJ1-AB12", "Antila", "27", 360, 2012, 8, 8.4, 37, "plaski ster", "tak", 3)
lodka3 = Zaglowka("LJ1-AB13", "Antila", "27", 390, 2017, 8, 8.4, 38, "plaski ster", "tak", 3)
lodka4 = Zaglowka("LJ1-AB14", "Antila", "27", 450, 2020, 8, 8.4, 37, "plaski ster", "tak", 3)
lodka5 = Zaglowka("LJ2-AB11", "Antila", "30", 410, 2015, 8, 11, 42, "kolo sterowe", "tak", 3)
lodka6 = Zaglowka("LJ2-AB12", "Antila", "30", 500, 2020, 8, 11, 44, "kolo sterowe", "tak", 3)
lodka7 = Zaglowka("LJ3-AB11", "Twister", "26", 350, 2015, 6, 8, 36, "plaski ster", "tak", 2)
lodka8 = Zaglowka("LJ3-AB12", "Twister", "26", 370, 2019, 6, 8, 36, "plaski ster", "tak", 2)

lodka9 = Motorowka("LM1-AB-11", "Laguna", "700", 440, 2014, 6, 8.5, 55, "kolo sterowe", "tak", 15)
lodka10 = Motorowka("LM1-AB-12", "Laguna", "700", 470, 2017, 6, 8.5, 55, "kolo sterowe", "tak", 15)
lodka11 = Motorowka("LM1-AB-13", "Laguna", "700", 520, 2020, 6, 9, 50, "kolo sterowe", "tak", 20)
lodka12 = Motorowka("LM2-AB-11", "Calipso", "750", 500, 2018, 10, 5, 43, "kolo sterowe", "tak", 30)
lodka13 = Motorowka("LM3-AB-11", "Solar", "23", 400, 2012, 4, 7.3, 46, "kolo sterowe", "nie", 15)
lodka14 = Motorowka("LM3-AB-12", "Solar", "23", 460, 2016, 4, 7.3, 46, "kolo sterowe", "nie", 15)

W1.dodaj_lodke(lodka1)
W1.dodaj_lodke(lodka2)
W1.dodaj_lodke(lodka3)
W1.dodaj_lodke(lodka4)
W1.dodaj_lodke(lodka5)
W1.dodaj_lodke(lodka6)
W1.dodaj_lodke(lodka7)
W1.dodaj_lodke(lodka8)
W1.dodaj_lodke(lodka9)
W1.dodaj_lodke(lodka10)
W1.dodaj_lodke(lodka11)
W1.dodaj_lodke(lodka12)
W1.dodaj_lodke(lodka13)
W1.dodaj_lodke(lodka14)

lodka13.czy_wolne(date.today(), date.fromisoformat('2021-12-04'))
lodka13.wypisz_wolne("2021", "12")
lodka13.kal.najblizszy_rok[date.fromisoformat('2021-12-02')] = "zajete"
lodka13.czy_wolne(date.today(), date.fromisoformat('2021-12-04'))

lodka13.wypisz_wolne("2021", "12")

kal = Kalendarz()

# print(kal.najblizszy_rok)

print("Witaj! Jak możemy Ci pomoc?")
print("1. Chce zarezerwować samochód.")
print("2. Chce zarezerwować lodke.")
lodka_czy_auto = int(input("Wybierz numer: "))
twoj_prac = random.choice(W1.lp)
twoj_prac.przedstaw_sie()

if lodka_czy_auto == 1: #chcemy samochod
    print("Chcesz zobaczyc wszystkie dostepne samochody, czy szukasz czegos konkretnego?")
    print("1. Pokaz dostepne samochody")
    print("2. Szukam czegos konkretnego")
    wszystkie_czy_konkret = int(input("Twój wybor: "))
    if wszystkie_czy_konkret == 1:
        W1.ile_samochodow()
        W1.wypisz_samochody()
    elif wszystkie_czy_konkret == 2:
        print("Wpisz dane, które cie interesuja, jeśli jest Ci to obojetne to nie wpisuj nic:")

        marka = input("Marka samochodu: ")
        model = input("Model samochodu: ")
        rok = input("Rok produkcji: ")
        pasa = input("Ile maksymalnie pasazerow: ")
        drzwi = input("Ilu drzwiowy: ")
        biegi = input("Jaka skrzynia biegow (automat/manual): ")

        print("W podanej konfiguracji mamy takie samochody:")
        W1.szukaj_auta(model, marka, rok, pasa, drzwi, biegi)

elif lodka_czy_auto == 2: #chcemy lodke
    print("Jaka lodz?")
    print("1. zaglowa")
    print("2. motorowa")
    zag_czy_moto = int(input("Wybierz rodzaj lodzi i wpisz odpowiadajacy mu numer: "))
    if zag_czy_moto == 1: #lodka zaglowa
        print("Chcesz zobaczyc dostepne lodki zaglowe, czy szukasz czegos konkretnego?")
        print("1. Pokaz dostepne")
        print("2. Szukam czegos konkretnego")
        wszystkie_czy_konkret = int(input("Twój wybor: "))
        if wszystkie_czy_konkret == 1:
            W1.wypisz_lodki("zagl")
        elif wszystkie_czy_konkret == 2:
            print("Wpisz dane, które cie interesuja, jeśli jest Ci to obojetne to nie wpisuj nic:")    
            marka = input("Marka lodzi: ")
            model = input("Model lodzi: ")
            rok = input("Rok produkcji: ")
            pasa = input("Ile maksymalnie pasazerow: ")
            patent = input("Masz patent? (tak/nie): ")
            print("W podanej konfiguracji mamy takie samochody:")
            print(W1.szukaj_lodki_zagle(model, marka, rok, pasa, patent))

    elif zag_czy_moto == 2: #lodki motorowe
        print("Chcesz zobaczyc dostepne lodki motorowe, czy szukasz czegos konkretnego?")
        print("1. Pokaz dostepne")
        print("2. Szukam czegos konkretnego")
        wszystkie_czy_konkret = int(input("Twój wybor: "))
        if wszystkie_czy_konkret == 1:
            W1.wypisz_lodki("moto")
        elif wszystkie_czy_konkret == 2:
            print("Wpisz dane, które cie interesuja, jeśli jest Ci to obojetne to nie wpisuj nic:")            
            marka = input("Marka lodzi: ")
            model = input("Model lodzi: ")
            rok = input("Rok produkcji: ")
            pasa = input("Ile maksymalnie pasazerow: ")
            patent = input("Masz patent? (tak/nie): ")
            print("W podanej konfiguracji mamy takie samochody:")
            print(W1.szukaj_lodki_motor(model, marka, rok, pasa, patent))


print("Jeśli któryś samochód/łódka Ci sie spodobał, podaj jego kod, by zobaczyć szczegółowe informacje na jego temat")
nr = input("Wpisz kod: ")

for i in W1.lj.keys():
    if i == nr:
        print(W1.lj[i].wazne_info())
