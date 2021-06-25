import unittest
from jednostki import *
from ludzie import *
from wypozyczalnia import *
import sys
import random
import main

class Testy(unittest.TestCase):
    def setUp(self):
        self.W1 = Wypozyczalnia("1", "Wrocław")
        self.p1 = Pracownik(1, "Tomasz", "Janusz")
        self.p2 = Pracownik(2, "Mateusz", "Rabiega")
        self.p3 = Pracownik(3, "Kamil", "Pajak")
        self.p4 = Pracownik(4, "Marta", "Palma")

        self.W1.dodaj_pracownika(self.p1)
        self.W1.dodaj_pracownika(self.p2)
        self.W1.dodaj_pracownika(self.p3)
        self.W1.dodaj_pracownika(self.p4)

        self.auto1 = Samochod("S1-AB11", "Volkswagen", "Touran", 500, 2014, 7, 5, 140, 5, "manual")
        self.auto2 = Samochod("S2-AB11", "Suziki", "Ignis", 350, 2009, 5, 5, 90, 4.5, "manual")
        self.auto3 = Samochod("S3-AB11", "Toyota", "Aygo", 400, 2016, 5, 5, 110, 6, "manual")
        self.auto4 = Samochod("S3-AB12", "Toyota", "Aygo", 400, 2016, 5, 5, 110, 6, "automat")
        self.auto5 = Samochod("S4-AB11", "Opel", "Insygnia", 470, 2011, 5, 5, 120, 7, "manual")
        self.auto6 = Samochod("S5-AB11", "Toyota", "Aygo", 400, 2016, 5, 5, 110, 6, "manual")

        self.W1.dodaj_auto(self.auto1)
        self.W1.dodaj_auto(self.auto2)
        self.W1.dodaj_auto(self.auto3)
        self.W1.dodaj_auto(self.auto4)
        self.W1.dodaj_auto(self.auto5)
        self.W1.dodaj_auto(self.auto6)

        self.lodka1 = Zaglowka("LJ1-AB11", "Antila", "27", 360, 2012, 8, 8.4, 38, "plaski ster", "tak", 3)
        self.lodka2 = Zaglowka("LJ1-AB12", "Antila", "27", 360, 2012, 8, 8.4, 37, "plaski ster", "tak", 3)
        self.lodka3 = Zaglowka("LJ1-AB13", "Antila", "27", 390, 2017, 8, 8.4, 38, "plaski ster", "tak", 3)
        self.lodka4 = Zaglowka("LJ1-AB14", "Antila", "27", 450, 2020, 8, 8.4, 37, "plaski ster", "tak", 3)
        self.lodka5 = Zaglowka("LJ2-AB11", "Antila", "30", 410, 2015, 8, 11, 42, "kolo sterowe", "tak", 3)
        self.lodka6 = Zaglowka("LJ2-AB12", "Antila", "30", 500, 2020, 8, 11, 44, "kolo sterowe", "tak", 3)
        self.lodka7 = Zaglowka("LJ3-AB11", "Twister", "26", 350, 2015, 6, 8, 36, "plaski ster", "tak", 2)
        self.lodka8 = Zaglowka("LJ3-AB12", "Twister", "26", 370, 2019, 6, 8, 36, "plaski ster", "tak", 2)

        self.lodka9 = Motorowka("LM1-AB11", "Laguna", "700", 440, 2014, 6, 8.5, 55, "kolo sterowe", "tak", 15)
        self.lodka10 = Motorowka("LM1-AB12", "Laguna", "700", 470, 2017, 6, 8.5, 55, "kolo sterowe", "tak", 15)
        self.lodka11 = Motorowka("LM1-AB13", "Laguna", "700", 520, 2020, 6, 9, 50, "kolo sterowe", "tak", 20)
        self.lodka12 = Motorowka("LM2-AB11", "Calipso", "750", 500, 2018, 10, 5, 43, "kolo sterowe", "tak", 30)
        self.lodka13 = Motorowka("LM3-AB11", "Solar", "23", 400, 2012, 4, 7.3, 46, "kolo sterowe", "nie", 15)
        self.lodka14 = Motorowka("LM3-AB12", "Solar", "23", 460, 2016, 4, 7.3, 46, "kolo sterowe", "nie", 15)

        self.W1.dodaj_lodke(self.lodka1)
        self.W1.dodaj_lodke(self.lodka2)
        self.W1.dodaj_lodke(self.lodka3)
        self.W1.dodaj_lodke(self.lodka4)
        self.W1.dodaj_lodke(self.lodka5)
        self.W1.dodaj_lodke(self.lodka6)
        self.W1.dodaj_lodke(self.lodka7)
        self.W1.dodaj_lodke(self.lodka8)
        self.W1.dodaj_lodke(self.lodka9)
        self.W1.dodaj_lodke(self.lodka10)
        self.W1.dodaj_lodke(self.lodka11)
        self.W1.dodaj_lodke(self.lodka12)
        self.W1.dodaj_lodke(self.lodka13)
        self.W1.dodaj_lodke(self.lodka14)
    def test_max_osob(self):
        self.assertEqual(self.auto1.max_osob(), "Maksymalna liczba osob w pojezdzie to: 7")
        self.assertEqual(self.auto3.max_osob(), "Maksymalna liczba osob w pojezdzie to: 5")
        self.assertEqual(self.lodka4.max_osob(), "Komfortowa liczba osob to 8, a maksywalna to 10")
        self.assertEqual(self.lodka10.max_osob(), "Komfortowa liczba osob to 6, a maksywalna to 8")
        
    def test_znajdz_klienta(self):
        self.k = Klient("Jan", "Kowalski")
        self.assertEqual(self.W1.znajdz_klienta(self.k), False)
        self.W1.dodaj_klienta(self.k)
        self.assertEqual(self.W1.znajdz_klienta(self.k), self.k)

    def test_czy_wolne(self):
        self.k = Klient("Jan", "Kowalski")
        self.assertTrue(self.lodka4.czy_wolne("2021-07-03","2021-07-20"))
        self.W1.lodka4.rezerwacja("2021-07-13", "2021-07-28", self.k)
        self.assertFalse(self.lodka4.czy_wolne("2021-07-03","2021-07-20"))
        self.assertTrue(self.auto1.czy_wolne("2021-12-20","2021-12-30"))
        self.W1.auto1.rezerwacja("2021-12-22", "2021-12-23", self.k)
        self.assertFalse(self.auto1.czy_wolne("2021-12-20","2021-12-25"))

    def test_rezerwacja(self):
        self.k = Klient("Jan", "Kowalski")
        self.assertTrue(self.W1.auto2.rezerwacja("2021-12-22", "2021-12-23", self.k))
        self.assertFalse(self.W1.auto2.rezerwacja("2021-12-22", "2021-12-23", self.k))

    def test_cena_za_wynajem(self):
        self.k = Klient("Jan", "Kowalski")
        self.W1.dodaj_klienta(self.k)
        self.W1.lodka4.rezerwacja("2021-07-10", "2021-07-20", self.k)
        self.W1.lodka5.rezerwacja("2021-07-10", "2021-07-20", self.k)
        self.assertEqual(self.cena_za_wynajem(self.W1), 10460)

if __name__ == "__main__":
    unittest.main()





