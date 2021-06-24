from wypozyczalnia import Kalendarz

class Jednostka():
    def __init__(self, nazwa,  marka, model, cena_za_dobe, rok_produkcji, liczba_pasazerow):
        self.nazwa = nazwa
        self.marka = marka
        self.model = model
        self.cena = cena_za_dobe
        self.rok = rok_produkcji
        self.pasazerowie = liczba_pasazerow
        self.kal = Kalendarz()
    def czy_wolne(self, pocz, kon):
        self.kal.czy_wolne(pocz, kon)
    

class Samochod(Jednostka):
    def __init__(self, nazwa, marka, model, cena_za_dobe, rok_produkcji, liczba_pasazerow, liczba_drzwi, moc_silnika, spalanie, skrzynia_biegow):
        Jednostka.__init__(self, nazwa, marka, model, cena_za_dobe, rok_produkcji, liczba_pasazerow)
        self.drzwi = liczba_drzwi
        self.moc = moc_silnika
        self.spalanie = spalanie
        self.skrzynia = skrzynia_biegow

    def wazne_info(self):
        return "Samochod: {} {} z {} (skrzynia biegow {}), ma miejsca na {} i jest {} drzwiowy. Moc jego silnika to {}KM, " \
               "a spalanie ma na poziomie {}l/100km".format(self.marka, self.model, self.rok, self.skrzynia, self.pasazerowie,
                                                            self.drzwi, self.moc, self.spalanie)

    def info(self):
        return [self.nazwa, self.marka, self.model, self.rok, self.pasazerowie, self.drzwi, self.skrzynia]

    def max_osob(self):
        return "Maksymalna liczba osob w pojezdzie to: {}".format(self.pasazerowie)


class Lodka(Jednostka):
    def __init__(self, nazwa, marka, model, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent):
        Jednostka.__init__(self, nazwa, marka, model, cena_za_dobe, rok_produkcji, liczba_pasazerow)
        self.dlu = dlugosc
        self.max_zanu = max_zanurzenia
        self.ster = typ_steru
        self.patent = patent

    def info(self):
        return [self.nazwa, self.marka, self.model, self.rok, self.pasazerowie, self.patent]

    def czy_patent(self):
        if self.patent == "nie":
            return False
        if self.patent >= "tak":
            return True


class Zaglowka(Lodka):
    def __init__(self, nazwa, marka, model, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent, liczba_koi):
        Lodka.__init__(self, nazwa, marka, model, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent)
        self.koje = liczba_koi

    def max_osob(self):
        return "Komfortowa liczba osob to {}, a maksywalna to {}".format(self.pasazerowie, self.pasazerowie+2)

    def wazne_info(self):
        return "Lódź zaglowa: {} {} z roku {} ma miejsca na {} przy czym {} koi. Długość całkowita to {}m, " \
               "maksymalne zanurzenie {}cm, mamy tutaj {}. Czy potrzeba mieć patent by wypożyczyć łódź? {}".format(self.model, self.marka, self.rok, self.pasazerowie,
                                                                                                                 self.koje, self.dlu, self.max_zanu, self.ster, self.patent)


class Motorowka(Lodka):
    def __init__(self, nazwa, marka, model, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent, silnik):
        Lodka.__init__(self, nazwa, marka, model, cena_za_dobe, rok_produkcji, liczba_pasazerow, dlugosc, max_zanurzenia, typ_steru, patent)
        self.moc = silnik

    def max_osob(self):
        return "Maksymalna liczba osob to: {}".format(self.pasazerowie)

    def wazne_info(self):
        return "Lódź motorowa: {} {} z roku {} ma miejsca na {}. Długość całkowita to {}m, " \
               "maksymalne zanurzenie {}cm, mamy tutaj {} i silnik o mocy {}KM. Czy potrzeba mieć patent by wypożyczyć łódź? {}".format(self.model, self.marka, self.rok,
                                                                                                                                    self.pasazerowie, self.dlu, self.max_zanu,
                                                                                                                                    self.ster, self.moc,self.patent)
