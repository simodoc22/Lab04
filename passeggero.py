class Passeggero:
    def __init__(self,numero_univoco,nome,cognome):
        self.numero_univoco = str(numero_univoco)
        self.nome = str(nome)
        self.cognome = str(cognome)
        self.cabina = ""
    def assegna_cabina(self,codice_cabina):
        self.cabina = codice_cabina
    def __str__(self):
        return f"{self.numero_univoco} {self.nome} {self.cognome} {self.cabina}"