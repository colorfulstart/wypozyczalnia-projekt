import random
import copy

class Wypozyczalnia():
    def __init__(self, nr_wypozyczalni, lokalizacja):
        self.nr = nr_wypozyczalni
        self.lok = lokalizacja
        self.lj = {} #słownik jednstek
        self.ls = [] #lista samochodów
        self.ll = [] #lista lodek
        self.lp = [] #lista pracownikow
        self.lsk = [] #lista stalych klientow
        self.rez = [] #lista rezerwacji

    def wypisywanie_list(self, tab, auto_czy_lodz):
        format_rzedu ="{:>12}"
        if auto_czy_lodz == "auto":
            t = ["KOD:", "MARKA:", "MODEL:", "ROCZNIK:", "MAX PASAŻ.:", "DRZWI:", "SKRZYNIA:"]
            format_rzedu ="{:>12}" * len(t)
            print(format_rzedu.format( *t))
        elif auto_czy_lodz == "lodz":
            t = ["KOD:", "MARKA:", "MODEL:", "ROCZNIK:", "MAX PASAŻ.:", "PATENT:"]
            format_rzedu ="{:>12}" * len(t)
            print(format_rzedu.format( *t))
        for i in tab:
            print(format_rzedu.format( *i.info()))

    def wypisz_lokalizacje(self):
        print(f"Wypozyczalnia nr {self.nr} znajduje sie w {self.lok}")

    def ile_samochodow(self):
        print(f"W Wypozyczalni nr {self.nr} mamy dostępne {len(self.ls)} samochody")

    def wypisz_samochody(self):
        self.wypisywanie_list(self.ls,"auto")

    def ile_lodek(self):
        print(f"W Wypozyczalni nr {self.nr} mamy dostępne {self.ll} lodek")
    
    def wypisz_lodki(self, jaka):
        tab = []
        if jaka == "moto":
            for i in self.ll:
                if "M" in i.nazwa:
                    tab.append(i)
        elif jaka == "zagl":
            for i in self.ll:
                if "J" in i.nazwa:
                    tab.append(i)
        self.wypisywanie_list(tab,"lodz")

    def ile_pracownikow(self):
        print(f"W Wypozyczalni nr {self.nr} pracuja {self.lp} osob")

    def ile_stalych_klientow(self):
        print(f"Wypozyczalnia nr {self.nr} ma {len(self.lsk)} stałych klientow")

    def pracow(self):
        return self.lp

    def dodaj_pracownika(self, pracownik):
        self.lp.append(pracownik)

    def dodaj_auto(self, auto):
        self.ls.append(auto)
        self.lj[auto.nazwa] = auto

    def dodaj_lodke(self,lodka):
        self.ll.append(lodka)
        self.lj[lodka.nazwa] = lodka

    def szukaj_auta(self, model_new, marka_new, rok_new, pasazerowie_new, drzwi_new, skrzynia_new): #done
        tab = []
        for i in self.ls:
            if model_new == i.model or marka_new == i.marka or rok_new == i.rok or \
                    pasazerowie_new == i.pasazerowie or drzwi_new == i.drzwi or skrzynia_new == i.skrzynia:
                if i not in tab:
                    tab.append(i)
        if len(tab) == 0:
            print("Nie ma takich samochodow :(")
        else:
            self.wypisywanie_list(tab,"auto")


    def szukaj_lodki_zagle(self, model_new, marka_new, rok_new, pasa_new, patent): #done
        tab = []
        for i in self.ll:
            if "J" in i.nazwa and (model_new == i.model or marka_new == i.marka or rok_new == i.rok or \
                    pasa_new == i.pasazerowie or patent == i.patent):
                if i not in tab:
                    tab.append(i)

        if len(tab) == 0:
            print("Nie ma takich lodek :(")
        else:
            self.wypisywanie_list(tab,"lodz")

    def szukaj_lodki_motor(self, model_new, marka_new, rok_new, pasa_new, patent): #done
        tab = []
        for i in self.ll:
            if "M" in i.nazwa and (model_new == i.model or marka_new == i.marka or rok_new == i.rok or \
                    pasa_new == i.pasazerowie or patent == i.patent):
                if i not in tab:
                    tab.append(i)

        if len(tab) == 0:
            print("Nie ma takich lodek :(")
        else:
            self.wypisywanie_list(tab,"lodz")





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


class Kalendarz():
    def __init__(self):
        self.kal = []



    #def czy_dostepne(self, ):
