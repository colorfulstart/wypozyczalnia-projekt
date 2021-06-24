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
        return "Samochod: {} {} z {} (skrzynia biegow {}), ma miejsca na {} i jest {} drzwiowy. Moc jego silnika to {}, a spalanie ma na poziomie {}l/100km".format(self.model, self.marka, self.rok,
                                                                                                          self.skrzynia, self.pasazerowie,self.drzwi, self.moc, self.spalanie)

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

