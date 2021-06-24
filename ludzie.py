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


class Pracownik():
    def __init__(self, nr_pracownika, imie, nazwisko):
        self.nr = nr_pracownika
        self.imie = imie
        self.nazw = nazwisko

    def dane_pracownika(self):
        return "Pracownik nr {}: {} {}".format(self.nr, self.imie, self.nazw)
