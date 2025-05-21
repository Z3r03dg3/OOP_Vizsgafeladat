import os
import time

from classes.Auto import *
from classes.Szemelyauto import *
from classes.Teherauto import *
from classes.Autokolcsonzo import *
from classes.Berles import *

autokolcsonzo = Autokolcsonzo()

berles1 = Berles("2025-04-20","Dániel")
berles2 = Berles("2025-03-05","Gergő")
berles3 = Berles("2025-03-20","Linda")
berles4 = Berles("2025-05-12","Sára")

tesztauto1 = Teherauto("HKJ-876", "50000")
tesztauto1.berlesek.append(berles1)
autokolcsonzo.autok.append(tesztauto1)

tesztauto2 = Teherauto("GHU-295", "10000")
tesztauto2.berlesek.append(berles2)
autokolcsonzo.autok.append(tesztauto2)

tesztauto3 = Szemelyauto("PHD-394", "30000")
tesztauto3.berlesek.append(berles3)
tesztauto3.berlesek.append(berles4)
autokolcsonzo.autok.append(tesztauto3)


while True:
    print("Válasszon az alábbiak közül: \n1. Autó bérlése \n2. Bérlés lemondása \n3. Bérlések listázása \n4. Kilépés")
    valasz = input()
    print("\n")
    if valasz == "1":
        autokolcsonzo.auto_berlese()
    elif valasz == "2":
        autokolcsonzo.auto_berles_lemondasa()
    elif valasz == "3":
        autokolcsonzo.autok_berlesek_listazasa()
    elif valasz == "4":
        print("Köszönjük hogy a Dániel Autókölcsönzőt választotta. Viszlát! ")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        print("Próbálja újra")
        continue