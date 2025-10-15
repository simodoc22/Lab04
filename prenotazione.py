class Prenotazione:
    def __init__(self, codice_cabina,codice_passeggero):
        self.codice_cabina = codice_cabina
        self.codice_passeggero = codice_passeggero
    def __str__(self):
        return f'{self.codice_cabina} {self.codice_passeggero}'
