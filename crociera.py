from cabina import Cabina,Deluxe,CabinaAnimali
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self.lista_passeggeri= []
        self.lista_cabine = []



    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        cabine = self.lista_cabine
        passeggeri = self.lista_passeggeri
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                for line in infile:
                    riga = line.split().strip()
                    if len(riga)==4 and riga[4]==str():
                        codice, numero_letti, numero_ponte, prezzo,tipologia = riga
                        new_cabina = Deluxe(codice,numero_letti,numero_ponte,prezzo,tipologia)
                        cabine.append(new_cabina)
                    elif len(riga)==2:
                        codice_univoco,nome,cognome= riga
                        new_passeggero = Passeggero(codice_univoco,nome,cognome)
                        passeggeri.append(new_passeggero)
                    elif len(riga) == 3:
                        codice, numero_letti, numero_ponte, prezzo = riga
                        new_cabina = Cabina(codice,numero_letti,numero_ponte,prezzo)
                        cabine.append(new_cabina)
                    else:
                        codice, numero_letti, numero_ponte, prezzo, numero_max = riga
                        new_cabina = CabinaAnimali(codice,numero_letti,numero_ponte,prezzo,numero_max)
                        cabine.append(new_cabina)
        except FileNotFoundError:
            print('file non trovato')


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

