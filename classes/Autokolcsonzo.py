from classes.Berles import *
from datetime import datetime, timedelta

class Autokolcsonzo:
    kolcsonzo_neve = "Daniel Autókölcsönző"

    def __init__(self):
        self.autok = []

    def autok_berlesek_listazasa(self):
        for auto in self.autok:
            print(f"{auto.rendszam} {auto.berleti_dij}")
            for berles in auto.berlesek:
                print(f"{berles.datum} {berles.nev}")
            print("\n")

    def auto_berlese(self):
        print("Az autó bérléséhez írja be a kívánt sorszámot")
        print("Sorszám    Típus     Rendszám     Bérleti díj/Nap")

        for index, auto in enumerate(self.autok):
            print(f"{index}.    {auto.tipus}    {auto.rendszam}    {auto.berleti_dij}")

        try:
            auto_kival = int(input(f"Válassza ki a bérelendő autó sorszámát 0-{len(self.autok) - 1}: "))
            if auto_kival < 0 or auto_kival >= len(self.autok):
                print("Ilyen sorszám nem létezik.")
                return
        except ValueError:
            print("Nem számot írt be.")
            return

        berlo_nev = input("Adja meg a bérlő nevét: ").strip()
        if not berlo_nev:
            print("A név nem lehet üres.")
            return

        while True:
            today = datetime.today().strftime("%Y-%m-%d")
            ber_datum = input(f"Adja meg a bérlés dátumát ebben a formátumban: YYYY-MM-DD [{today}]: ").strip()
            if ber_datum == "":
                ber_datum = today

            try:
                datetime.strptime(ber_datum, "%Y-%m-%d")
            except ValueError:
                print("Rossz formátum")
                continue

            foglalt_datumok = [berles.datum for berles in self.autok[auto_kival].berlesek]

            if ber_datum not in foglalt_datumok:
                self.autok[auto_kival].berlesek.append(Berles(ber_datum, berlo_nev))
                print(f"Sikeres bérlés: {ber_datum}, név: {berlo_nev}")
                break
            else:
                print(f"Ez az autó már foglalt {ber_datum}-ra!")
                print("Ajánlott szabad napok:")

                ajanlott_napok = []
                datum = datetime.strptime(ber_datum, "%Y-%m-%d")
                nap_szamlalo = 1
                while len(ajanlott_napok) < 3:
                    uj_datum = datum + timedelta(days=nap_szamlalo)
                    datum_str = uj_datum.strftime("%Y-%m-%d")
                    if datum_str not in foglalt_datumok:
                        ajanlott_napok.append(datum_str)
                    nap_szamlalo += 1

                for d in ajanlott_napok:
                    print(f"- {d}")

    def auto_berles_lemondasa(self):
        print("Sorszám  Típus  Rendszám  Bérleti díj/Nap")
        auto_berles_lemondas_lista = []

        for index_auto, auto in enumerate(self.autok):
            print(f"{index_auto}.    {auto.tipus}    {auto.rendszam}    {auto.berleti_dij}")
            for index_berles, berles in enumerate(auto.berlesek):
                print(f"    {index_berles}. {berles.datum} {berles.nev}")
            auto_berles_lemondas_lista.append([index_auto, auto])

        try:
            auto_kival = int(input(f"Adja meg az autó sorszámát 0-{len(auto_berles_lemondas_lista) - 1}: "))
            berles_kival = int(input("Adja meg a bérlés sorszámát amit lemondani kíván: "))

            if 0 <= auto_kival < len(auto_berles_lemondas_lista):
                auto = auto_berles_lemondas_lista[auto_kival][1]
                if 0 <= berles_kival < len(auto.berlesek):
                    auto.berlesek.pop(berles_kival)
                    print("Bérlés sikeresen lemondva")
                else:
                    print("Nincs ilyen bérlés sorszám")
            else:
                print("Nincs ilyen autó sorszám")
        except ValueError:
            print("Érvénytelen bemenet. Csak számot írjon be")
