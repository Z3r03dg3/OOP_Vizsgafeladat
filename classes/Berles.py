class Berles:
    def __init__(self, datum: str, nev: str):
        self.datum = datum
        self.nev = nev

    def __str__(self):
        return f"{self.datum} - Bérlő: {self.nev}"
