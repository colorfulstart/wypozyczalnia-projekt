from jednostki import *
from ludzie import *
from wypozyczalnia import *

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
W1.lp.append(p1.dane_pracownika())
W1.lp.append(p2.dane_pracownika())
W1.lp.append(p3.dane_pracownika())
W1.lp.append(p4.dane_pracownika())
print(W1.ile_pracownikow())
#print(W1.lp)
#print(P1.dane_pracownika())

#cena_za_dobe, rok_produkcji, liczba_pasazerow, liczba_drzwi, moc_silnika, spalanie, skrzynia_biegow
auto1 = Samochod("S1-AB11", "Touran", "Volkswagen", 500, 2014, 7, 5, 140, 5, "manual")
auto2 = Samochod("S2-AB11", "Ignis", "Suziki", 350, 2009, 5, 5, 90, 4.5, "manual")
auto3 = Samochod("S3-AB11", "Aigo", "Toyota", 400, 2016, 5, 5, 110, 6, "manual")
auto4 = Samochod("S3-AB12", "Aigo", "Toyota", 400, 2016, 5, 5, 110, 6, "automat")
auto5 = Samochod("S4-AB11", "Insygnia", "Opel", 470, 2011, 5, 5, 120, 7, "manual")
auto6 = Samochod("S5-AB11", "Aigo", "Toyota", 400, 2016, 5, 5, 110, 6, "manual")

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


W1.dodaj_jednostke("S1-AB11", auto1)
W1.dodaj_jednostke("S2-AB11", auto2)
W1.dodaj_jednostke("S3-AB11", auto3)
W1.dodaj_jednostke("S3-AB12", auto4)
W1.dodaj_jednostke("S4-AB11", auto5)
W1.dodaj_jednostke("S5-AB11", auto6)

W1.dodaj_jednostke("LJ1-AB11", lodka1)
W1.dodaj_jednostke("LJ1-AB12", lodka2)
W1.dodaj_jednostke("LJ1-AB13", lodka3)
W1.dodaj_jednostke("LJ1-AB14", lodka4)
W1.dodaj_jednostke("LJ2-AB11", lodka5)
W1.dodaj_jednostke("LJ2-AB12", lodka6)
W1.dodaj_jednostke("LJ3-AB11", lodka7)
W1.dodaj_jednostke("LJ3-AB12", lodka8)

W1.dodaj_jednostke("LM1-AB-11", lodka9)
W1.dodaj_jednostke("LM1-AB-12", lodka10)
W1.dodaj_jednostke("LM1-AB-13", lodka11)
W1.dodaj_jednostke("LM2-AB-11", lodka12)
W1.dodaj_jednostke("LM3-AB-11", lodka13)
W1.dodaj_jednostke("LM3-AB-12", lodka14)


#print(W1.lj)

#'''
print("Witaj! Jak możemy Ci pomoc?")
print("1. Chce zarezerwować samochód.")
print("2. Chce zarezerwować lodke.")
co1 = int(input("Wybierz numer: "))

if co1 == 2: #chcemy lodke
    twoj_prac = random.choice(W1.lp)
    print("W wyborze pomoze ci: {}.".format(twoj_prac))

    print("Jaka lodz?")
    print("1. zaglowa")
    print("2. motorowa")
    co2 = int(input("Wybierz rodzaj lodzi i wpisz odpowiadajacy mu numer: "))
    if co2 == 1: #lodka zaglowa
        print("Chcesz zobaczyc dostepne lodki zaglowe, czy szukasz czegos konkretnego?")
        print("1. Pokaz dostepne")
        print("2. Szukam czegos konkretnego")
        co3 = int(input("Twój wybor: "))
        if co3 == 1:
            lista =[]
            for i in range(len(W1.ll)):
                if "J" in W1.ll[i][0]:
                    if W1.ll[i] not in lista:
                        lista.append(W1.ll[i])
            print(lista)
        else:
            print("Wpisz dane, które cie interesuja, jeśli jest Ci to obojetne to nie wpisuj nic:")

            model = input("Model lodzi: ")
            marka = input("Marka lodzi: ")
            rok = input("Rok produkcji: ")
            pasa = input("Ile maksymalnie pasazerow: ")
            patent = input("Masz patent? (tak/nie): ")
            print("W podanej konfiguracji mamy takie samochody:")
            print(W1.szukaj_lodki_zagle(model, marka, rok, pasa, patent))


    else: #lodki motorowe
        print("Chcesz zobaczyc dostepne lodki motorowe, czy szukasz czegos konkretnego?")
        print("1. Pokaz dostepne")
        print("2. Szukam czegos konkretnego")
        co3 = int(input("Twój wybor: "))
        if co3 == 1:
            lista = []
            for i in range(len(W1.ll)):
                if "M" in W1.ll[i][0]:
                    if W1.ll[i] not in lista:
                        lista.append(W1.ll[i])
            print(lista)
        else:
            print("Wpisz dane, które cie interesuja, jeśli jest Ci to obojetne to nie wpisuj nic:")

            model = input("Model lodzi: ")
            marka = input("Marka lodzi: ")
            rok = input("Rok produkcji: ")
            pasa = input("Ile maksymalnie pasazerow: ")
            patent = input("Masz patent? (tak/nie): ")
            print("W podanej konfiguracji mamy takie samochody:")
            print(W1.szukaj_lodki_motor(model, marka, rok, pasa, patent))


if co1 == 1: #chcemy samochod
    twoj_prac = random.choice(W1.lp)
    print("W wyborze pomoze ci: {}.".format(twoj_prac))

    print("Chcesz zobaczyc dostepne samochody, czy szukasz czegos konkretnego?")
    print("1. Pokaz dostepne samochody")
    print("2. Szukam czegos konkretnego")
    co3 = int(input("Twój wybor: "))
    if co3 == 1:
        print(W1.ile_samochodow())
        print(W1.ls)
    else:
        print("Wpisz dane, które cie interesuja, jeśli jest Ci to obojetne to nie wpisuj nic:")

        model = input("Model samochodu: ")
        marka = input("Marka samochodu: ")
        rok = input("Rok produkcji: ")
        pasa = input("Ile maksymalnie pasazerow: ")
        drzwi = input("Ilu drzwiowy: ")
        biegi = input("Jaka skrzynia biegow (automat/manual): ")

        print("W podanej konfiguracji mamy takie samochody:")
        print(W1.szukaj_auto(model, marka, rok, pasa, drzwi, biegi))

print("Jeśli któryś samochód/łódka Ci sie spodobał, podaj jego numer identyfikacyjny, by zobaczyć szczegółowe informacje na jego temat")
nr = input("Wpisz nr: ")

for i in W1.lj.keys():
    if i == nr:
        print(W1.lj[i].wazne_info())
