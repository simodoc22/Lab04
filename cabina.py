
class Cabina:
    def __init__(self,codice,numero_letti,numero_ponte,prezzo):
        self.codice = codice
        self.numero_letti = int(numero_letti)
        self.numero_ponte = int(numero_ponte)
        self.prezzo = int(prezzo)
        self.disponibilità = True


    def __str__(self):
        return f"{self.codice}-{self.numero_letti}-{self.numero_ponte}-{self.prezzo}"

    def disponibilità(self):
        self.disponibilità = False
    def calcolo_prezzo(self):
        self.prezzo = self.prezzo

class CabinaAnimali(Cabina):
    def __init__(self,codice,numero_letti,numero_ponte,prezzo,numero_animali):
        super().__init__(codice, numero_letti, numero_ponte, prezzo)
        self.numero_animali = int(numero_animali)
    def __str__(self):
        return f"{self.codice}-{self.numero_letti}-{self.numero_ponte}-{self.prezzo}-{self.numero_animali}"
    def calcolo_prezzo(self):
        self.prezzo = self.prezzo * (1+0.10*self.numero_animali)


class Deluxe(Cabina):
    def __init__(self,codice,numero_letti,numero_ponte,prezzo,tipologia):
        super().__init__(codice, numero_letti, numero_ponte, prezzo)
        self.tipologia = str(tipologia)
    def __str__(self):
        return(f"{self.codice}-{self.numero_letti}-{self.numero_ponte}-{self.prezzo}-{self.tipologia}")
    def calcolo_prezzo(self):
        self.prezzo = self.prezzo * 1.20

class Standard(Cabina):
    def __init__(self,codice,numero_letti,numero_ponte,prezzo):
        super().__init__(codice,numero_letti,numero_ponte,prezzo)







