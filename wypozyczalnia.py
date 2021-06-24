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

    def dodaj_jednostke(self, nr, jednostka):
        self.lj[nr] = jednostka




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


