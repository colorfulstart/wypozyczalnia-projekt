import random
import copy

class Jednostka():
    def __init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow):
        self.nazwa = nazwa
        self.model = model
        self.marka = marka
        self.cena = cena_za_dobe
        self.rok = rok_produkcji
        self.pasazerowie = liczba_pasazerow

class Samochody(Jednostka):
    def __init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, liczba_drzwi, moc_silnika, spalanie, skrzynia_biegow):
        Jednostka.__init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow)
        self.drzwi = liczba_drzwi
        self.moc = moc_silnika
        self.spalanie = spalanie
        self.skrzynia = skrzynia_biegow

    def wazne_info(self):
        return "Samochod: {} {} z {}, ma miejsca na {}".format(self.model, self.marka, self.rok, self.pasazerowie)

    def info(self):
        return [self.nazwa, self.model, self.marka, self.rok, self.pasazerowie, self.drzwi, self.skrzynia]

    def max_osob(self):
        return "Maksymalna liczba osob w pojezdzie to: {}".format(self.pasazerowie)





class Lodki(Jednostka):
    def __init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent):
        Jednostka.__init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow)
        self.dlu = dlugosc
        self.max_zanu = max_zanurzenia
        self.ster = typ_steru
        self.patent = patent

    def info(self):
        return [self.nazwa, self.model, self.marka, self.rok, self.pasazerowie, self.patent]

    def czy_patent(self):
        if self.patent == "nie":
            return False
        if self.patent >= "tak":
            return True


class Zagle(Lodki):
    def __init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent, liczba_koi):
        Lodki.__init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent)
        self.koje = liczba_koi

    def max_osob(self):
        return "Komfortowa liczba osob to {}, a maksywalna to {}".format(self.pasazerowie, self.pasazerowie+2)


class Motorowe(Lodki):
    def __init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent, silnik):
        Lodki.__init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent)
        self.moc = silnik

    def max_osob(self):
        return "Maksymalna liczba osob to: {}".format(self.pasazerowie)




class Klient():
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazw = nazwisko

    def dane_klienta(self):
        return "Klient: {} {}".format(self.imie, self.nazw)

'''
class staly_klient(klient):
    def __init__(self, imie, nazwisko, nazwa_uzytkownika, mail, patent, kiedy):
        klient.__init__(self, imie, nazwisko)
        self.nazwa = nazwa_uzytkownika
        self.mail = mail
        self.patent = patent
        self.data = kiedy
        self.znizka = 5
        self.wczesniejsze_rez = []

    def dane_klienta(self):
        return "{} - Staly klient od {}: {} {}".format(self.nazwa, self.data, self.imie, self.nazw)

    def zmien_nazwe(self, new_nazwa):
        self.nazwa = new_nazwa

    def zmien_imie(self, new_imie):
        self.imie = new_imie

    def zmien_nazwisko(self, new_nazw):
        self.nazw = new_nazw

    def zmien_mail(self, new_mail):
        self.mail = new_mail

    def jaki_patent(self):
        if self.patent == 0:
            return "Nie masz patentu"
        if self.patent == 1:
            return "Patent sternika jachtowego"
        if self.patent == 2:
            return "Patent sternika morskiego"
        if self.patent >= 3:
            return "Kapitan lub wyzej"

    def zmien_patent(self, new_patent):
        self.patent = new_patent

    def wczesniejsze_rezerwacje(self):
        return "Twoje wczesnijesze rezerwaje: \n {}".format(self.wczesniejsze_rezerwacje)

    def jaka_znizka(self):
        return "Uzytkownik {} ma znizke wysokosci {}%".format(self.nazwa, self.znizka)

    def zmien_znizke(self):
        procent = 0
        if len(self.wczesniejsze_rez) > 2:
            procent = self.znizka + len(self.wczesniejsze_rez)//2
        if procent > 16:
            procent = 15
        self.znizka = procent
'''


class Pracownicy():
    def __init__(self, nr_pracownika, imie, nazwisko):
        self.nr = nr_pracownika
        self.imie = imie
        self.nazw = nazwisko

    def dane_pracownika(self):
        return "Pracownik nr {}: {} {}".format(self.nr, self.imie, self.nazw)





class Wypozyczalnia():
    def __init__(self, nr_wypozyczalni, lokalizacja):
        self.nr = nr_wypozyczalni
        self.lok = lokalizacja
        self.lj = [] #lista jednstek
        self.ls = [] #lista samochodów
        self.ll = [] #lista lodek
        self.lp = [] #lista pracownikow
        self.lsk = [] #lista stalych klientow
        self.rez = [] #lista rezerwacji

    def gdzie(self):
        return "Wypozyczalnia nr {} znajduje sie w {}".format(self.nr, self.lok)

    def ile_samochodow(self):
        return "W Wypozyczalni nr {} mamy dostępne {} samochody".format(self.nr, len(self.ls))

    def ile_lodek(self):
        return "W Wypozyczalni nr {} mamy dostępne {} lodek".format(self.nr, len(self.ll))

    def ile_pracownikow(self):
        return "W Wypozyczalni nr {} pracuja {} osob".format(self.nr, len(self.lp))

    def ile_stalych_klientow(self):
        return "Wypozyczalnia nr {} ma {} stałych klientow".format(self.nr, len(self.lsk))

    def pracow(self):
        return self.lp

    def dodaj_auto(self, auto):
        self.ls.append(auto)

    def dodaj_lodke(self,lodka):
        self.ll.append(lodka)

    def szukaj_auto(self, model_new, marka_new, rok_new, pasazerowie_new, drzwi_new, skrzynia_new):
        lista = copy.copy(self.ls)
        tab = []

        for i in range(len(self.ls)):
            if model_new == self.ls[i][1] or marka_new == self.ls[i][2] or rok_new == self.ls[i][3] or \
                    pasazerowie_new == self.ls[i][4] or drzwi_new == self.ls[i][5] or skrzynia_new == self.ls[i][6]:
                if self.ls[i] not in tab:
                    tab.append(self.ls[i])

        if len(tab) == 0:
            return "Nie ma takich samochodow :("
        return tab


    def szukaj_lodki_zagle(self, model_new, marka_new, rok_new, pasa_new, patent):
        tab = []

        for i in range(len(self.ll)):
            if "J" in self.ll[i][0] and (model_new == self.ll[i][1] or marka_new == self.ll[i][2] or rok_new == self.ll[i][3] or \
                    pasa_new == self.ll[i][4] or patent == self.ll[i][4]):
                if self.ll[i] not in tab:
                    tab.append(self.ll[i])

        if len(tab) == 0:
            return "Nie ma takich lodek :("
        return tab

    def szukaj_lodki_motor(self, model_new, marka_new, rok_new, pasa_new, patent):
        tab = []

        for i in range(len(self.ll)):
            if "M" in self.ll[i][0] and (model_new == self.ll[i][1] or marka_new == self.ll[i][2] or rok_new == self.ll[i][3] or \
                    pasa_new == self.ll[i][4] or patent == self.ll[i][4]):
                if self.ll[i] not in tab:
                    tab.append(self.ll[i])

        if len(tab) == 0:
            return "Nie ma takich lodek :("
        return tab




class Rezerwacja():
    def __init__(self, nr, nazwa_uzytkownika, nr_sprzetu, od_kiedy, do_kiedy):
        self.nr = nr
        self.nazwa = nazwa_uzytkownika
        self.sprzet = nr_sprzetu
        self.od = od_kiedy
        self.do = do_kiedy
        self.lrez = [] #lista rezerwacji
        self.kasa = 0
'''
    def kwota(self): #tuatj musze pozamieniac!!!!
        self.kasa = (self.do - self.od)*self.sprzet.cena
        if self.nazwa in Wypozyczalnia.ile_stalych_klientow():
            self.kasa = self.kasa*staly_klient.jaka_znizka()
        return self.kasa
'''
    #def dodaj_rezerwacje(self):


class kalendarz():
    def __init__(self):
        self.kal = []



    #def czy_dostepne(self, ):


W1 = Wypozyczalnia("1", "Wrocław")
#print(w1.gdzie())
#print(w1.ile_lodek())

#jed1 = jednostka("S1-AB12", "opel", "insygnia", 400, 2003, 5)


#dodani pracownicy
p1 = Pracownicy(1, "Tomasz", "Janusz")
p2 = Pracownicy(2, "Mateusz", "Rabiega")
p3 = Pracownicy(3, "Kamil", "Pajak")
p4 = Pracownicy(4, "Marta", "Palma")
W1.lp.append(p1.dane_pracownika())
W1.lp.append(p2.dane_pracownika())
W1.lp.append(p3.dane_pracownika())
W1.lp.append(p4.dane_pracownika())
print(W1.ile_pracownikow())
#print(W1.lp)
#print(P1.dane_pracownika())

#cena_za_dobe, rok_produkcji, liczba_pasazerow, liczba_drzwi, moc_silnika, spalanie, skrzynia_biegow
auto1 = Samochody("S1-AB11", "Touran", "Volkswagen", 500, 2014, 7, 5, 140, 5, "manual")
auto2 = Samochody("S2-AB11", "Ignis", "Suziki", 350, 2009, 5, 5, 90, 4.5, "manual")
auto3 = Samochody("S3-AB11", "Aigo", "Toyota", 400, 2016, 5, 5, 110, 6, "manual")
auto4 = Samochody("S3-AB12", "Aigo", "Toyota", 400, 2016, 5, 5, 110, 6, "automat")
auto5 = Samochody("S4-AB11", "Insygnia", "Opel", 470, 2011, 5, 5, 120, 7, "manual")
auto6 = Samochody("S5-AB11", "Aigo", "Toyota", 400, 2016, 5, 5, 110, 6, "manual")

W1.dodaj_auto(auto1.info())
W1.dodaj_auto(auto2.info())
W1.dodaj_auto(auto3.info())
W1.dodaj_auto(auto4.info())
W1.dodaj_auto(auto5.info())
W1.dodaj_auto(auto6.info())


lodka1 = Zagle("LJ1-AB11", "Antila", "27", 360, 2012, 8, 8.4, 38, "plaski", "tak", 3)
lodka2 = Zagle("LJ1-AB12", "Antila", "27", 360, 2012, 8, 8.4, 37, "plaski", "tak", 3)
lodka3 = Zagle("LJ1-AB13", "Antila", "27", 390, 2017, 8, 8.4, 38, "plaski", "tak", 3)
lodka4 = Zagle("LJ1-AB14", "Antila", "27", 450, 2020, 8, 8.4, 37, "plaski", "tak", 3)
lodka5 = Zagle("LJ2-AB11", "Antila", "30", 410, 2015, 8, 11, 42, "kolo sterowe", "tak", 3)
lodka6 = Zagle("LJ2-AB12", "Antila", "30", 500, 2020, 8, 11, 44, "kolo sterowe", "tak", 3)
lodka7 = Zagle("LJ3-AB11", "Twister", "26", 350, 2015, 6, 8, 36, "plaski", "tak", 2)
lodka8 = Zagle("LJ3-AB12", "Twister", "26", 370, 2019, 6, 8, 36, "plaski", "tak", 2)


lodka9 = Motorowe("LM1-AB-11", "Laguna", "700", 440, 2014, 6, 8.5, 55, "kolo sterowe", "tak", 15)
lodka10 = Motorowe("LM1-AB-12", "Laguna", "700", 470, 2017, 6, 8.5, 55, "kolo sterowe", "tak", 15)
lodka11 = Motorowe("LM1-AB-13", "Laguna", "700", 520, 2020, 6, 9, 50, "kolo sterowe", "tak", 20)
lodka12 = Motorowe("LM2-AB-11", "Calipso", "750", 500, 2018, 10, 5, 43, "kolo sterowe", "tak", 30)
lodka13 = Motorowe("LM3-AB-11", "Solar", "23", 400, 2012, 4, 7.3, 46, "kolo sterowe", "nie", 15)
lodka14 = Motorowe("LM3-AB-12", "Solar", "23", 460, 2016, 4, 7.3, 46, "kolo sterowe", "nie", 15)

W1.dodaj_lodke(lodka1.info())
W1.dodaj_lodke(lodka2.info())
W1.dodaj_lodke(lodka3.info())
W1.dodaj_lodke(lodka4.info())
W1.dodaj_lodke(lodka5.info())
W1.dodaj_lodke(lodka6.info())
W1.dodaj_lodke(lodka7.info())
W1.dodaj_lodke(lodka8.info())
W1.dodaj_lodke(lodka9.info())
W1.dodaj_lodke(lodka10.info())
W1.dodaj_lodke(lodka11.info())
W1.dodaj_lodke(lodka12.info())
W1.dodaj_lodke(lodka13.info())
W1.dodaj_lodke(lodka14.info())


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
        biegi = input("Jaka skrzynia biegow: ")

        print("W podanej konfiguracji mamy takie samochody:")
        print(W1.szukaj_auto(model, marka, rok, pasa, drzwi, biegi))

print("Jeśli ktoras jednostka cię zainteresowała podaj jej numer identyfikacyjny, wtedy odslonia sie wszistkie dane")
nr = input("nr ")


#'''

