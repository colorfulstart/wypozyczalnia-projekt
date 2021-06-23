import random


class jednostka():
    def __init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow):
        self.nazwa = nazwa
        self.model = model
        self.marka = marka
        self.cena = cena_za_dobe
        self.rok = rok_produkcji
        self.pasazerowie = liczba_pasazerow

class samochody(jednostka):
    def __init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, liczba_drzwi, moc_silnika, spalanie, skrzynia_biegow, zasieg):
        jednostka.__init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow)
        self.drzwi = liczba_drzwi
        self.moc = moc_silnika
        self.spalanie = spalanie
        self.skrznia = skrzynia_biegow
        self.zasieg = zasieg

    def wazne_info(self):
        return "Samochod: {} {} z {}, ma miejsca na".format(self.model, self.marka, self.rok)

    def max_osob(self):
        return "Maksymalna liczba osob w pojezdzie to: {}".format(self.pasazerowie)


class lodki(jednostka):
    def __init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent):
        jednostka.__init__(self, nazwa, model, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow)
        self.dlu = dlugosc
        self.max_zanu = max_zanurzenia
        self.ster = typ_steru
        self.patent = patent

    def czy_patent(self):
        if self.patent == 0:
            return False
        if self.patent >= 1:
            return True


class zagle(lodki):
    def __init__(self, nazwa, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru,patent, liczba_koi):
        lodki.__init__(self, nazwa, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent)
        self.koje = liczba_koi

    def max_osob(self):
        return "Komfortowa liczba osob to {}, a maksywalna to {}".format(self.pasazerowie, self.pasazerowie+2)


class motorowe(lodki):
    def __init__(self, nazwa, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, patent, silnik):
        lodki.__init__(self, nazwa, marka, cena_za_dobe, rok_produkcji, liczba_pasazerow, patent)
        self.moc = silnik

    def max_osob(self):
        return "Maksymalna liczba osob to: {}".format(self.pasazerowie)




class klient():
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazw = nazwisko

    def dane_klienta(self):
        return "Klient: {} {}".format(self.imie, self.nazw)


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



class pracownicy():
    def __init__(self, nr_pracownika, imie, nazwisko):
        self.nr = nr_pracownika
        self.imie = imie
        self.nazw = nazwisko

    def dane_pracownika(self):
        return "Pracownik nr {}: {} {}".format(self.nr, self.imie, self.nazw)




class wypozyczalnia():
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




class rezerwacja():
    def __init__(self, nr, nazwa_uzytkownika, nr_sprzetu, od_kiedy, do_kiedy):
        self.nr = nr
        self.nazwa = nazwa_uzytkownika
        self.sprzet = nr_sprzetu
        self.od = od_kiedy
        self.do = do_kiedy
        self.lrez = [] #lista rezerwacji
        self.kasa = 0

    def kwota(self): #tuatj musze pozamieniac!!!!
        self.kasa = (self.do - self.od)*self.sprzet.cena
        if self.nazwa in wypozyczalnia.ile_stalych_klientow():
            self.kasa = self.kasa*staly_klient.jaka_znizka()
        return self.kasa

    #def dodaj_rezerwacje(self):


class kalendarz():
    def __init__(self):
        self.kal = []



    #def czy_dostepne(self, ):


w1 = wypozyczalnia("1", "Wrocław")
#print(w1.gdzie())
#print(w1.ile_lodek())

#jed1 = jednostka("S1-AB12", "opel", "insygnia", 400, 2003, 5)



p1 = pracownicy(1, "Tomasz", "Janusz")
p2 = pracownicy(2, "Mateusz", "Rabiega")
p3 = pracownicy(3, "Kamil", "Pajak")
p4 = pracownicy(4, "Marta", "Palma")
w1.lp.append(p1.dane_pracownika())
w1.lp.append(p2.dane_pracownika())
w1.lp.append(p3.dane_pracownika())
w1.lp.append(p4.dane_pracownika())
print(w1.ile_pracownikow())
#print(w1.lp)
#print(p1.dane_pracownika())


#'''
print("Witaj! Jak możemy Ci pomoc?")
print("1. Chce zarezerwować samochód.")
print("2. Chce zarezerwować lodke.")
co1 = int(input("Wybierz numer: "))

if co1 == 2:
    twoj_prac = random.choice(w1.lp)
    print("W wyborze pomoze ci: {}.".format(twoj_prac))

    print("Jaka lodz?")
    print("1. zaglowa")
    print("2. motorowa")
    co2 = int(input("Wybierz rodzaj lodzi i wpisz odpowiadajacy mu numer: "))
    if co2 == 1:


    else:


if co1 == 1:
    twoj_prac = random.choice(w1.lp)
    print("W wyborze pomoze ci: {}.".format(twoj_prac))

    print("Chcesz zobaczyc dostepne samochody, czy szukasz czegos konkretnego?")
    print("1. Pokaz dostepne samochody")
    print("2. Szukam czegos konkretnego")
    co3 = int(input("Twój wybor: "))
    if twoja stara = 0

#'''

