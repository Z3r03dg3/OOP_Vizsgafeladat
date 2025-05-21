from abc import ABC, abstractmethod

class Auto(ABC):
    @abstractmethod
    def __init__(self, rendszam: str, berleti_dij: int):
        self.rendszam = rendszam
        self.berleti_dij = int(berleti_dij)
        self.berlesek = []
