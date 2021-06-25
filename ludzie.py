class Klient():
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazw = nazwisko

    def dane_klienta(self):
        return "Klient: {} {}".format(self.imie, self.nazw)
    
    def cena_za_wynajem(self, wypo):
        suma = 0
        for i in wypo.lj.values():
            for j in i.kal.najblizszy_rok.values():
                if j == self:
                    suma += i.cena
        return suma


class Pracownik():
    def __init__(self, nr_pracownika, imie, nazwisko):
        self.nr = nr_pracownika
        self.imie = imie
        self.nazw = nazwisko

    def dane_pracownika(self):
        return "Pracownik nr {}: {} {}".format(self.nr, self.imie, self.nazw)

    def przedstaw_sie(self):
        print(f"Dzień dobry, jestem {self.imie} {self.nazw}. W czym mogę pomóc?")
