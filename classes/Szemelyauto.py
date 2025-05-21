from classes.Auto import *

class Szemelyauto(Auto):
    tipus = "Személyautó"

    def __init__(self, rendszam, berleti_dij):
        super().__init__(rendszam, berleti_dij)
