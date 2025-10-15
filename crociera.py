from cabina import Cabina,Deluxe,CabinaAnimali
from passeggero import Passeggero
from prenotazione import Prenotazione
class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self.lista_passeggeri= []
        self.lista_cabine = []
        self.lista_prenotazioni= []



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
                    riga = line.strip().split(",")
                    if len(riga)==5 and not riga[4].isdigit():
                        codice, numero_letti, numero_ponte, prezzo,tipologia = riga
                        new_cabina = Deluxe(codice,numero_letti,numero_ponte,prezzo,tipologia)
                        cabine.append(new_cabina)
                    elif len(riga)==3:
                        codice_univoco,nome,cognome= riga
                        new_passeggero = Passeggero(codice_univoco,nome,cognome)
                        passeggeri.append(new_passeggero)
                    elif len(riga) == 4:
                        codice, numero_letti, numero_ponte, prezzo = riga
                        new_cabina = Cabina(codice,numero_letti,numero_ponte,prezzo)
                        cabine.append(new_cabina)
                    elif len(riga) == 5 and riga[4].isdigit():
                        codice, numero_letti, numero_ponte, prezzo, numero_max = riga
                        new_cabina = CabinaAnimali(codice,numero_letti,numero_ponte,prezzo,numero_max)
                        cabine.append(new_cabina)
        except FileNotFoundError:
            print('file non trovato')


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        prenotazioni = self.lista_prenotazioni
        condizione = False
        condizione2= False
        condizione3= True
        condizione4= True
        for i in self.lista_passeggeri:
            if i.numero_univoco == codice_passeggero:
                condizione = True
        for i in self.lista_cabine:
            if i.codice == codice_cabina:
                condizione2 = True
        for i in prenotazioni:
            if i.codice_cabina == codice_cabina:
                condizione3 = False
        for i in prenotazioni:
            if i.codice_passeggero == codice_passeggero:
                condizione4= False
        if condizione==False or condizione2==False or condizione3==False or condizione4==False:
            raise Exception()
        else:
            prenotazione = Prenotazione(codice_cabina,codice_passeggero)
            prenotazioni.append(prenotazione)
            for i in self.lista_cabine:
                if i.codice == codice_cabina:
                    oggetto = i                ##utilizzo metodo disponibilità per aggiornare
                else:                           ##lo stato della cabina
                    pass
            oggetto.disponibilità()

    def cabine_ordinate_per_prezzo(self):
        for i in self.lista_cabine:
            i.calcolo_prezzo()
        return sorted(self.lista_cabine,key=lambda i: i.prezzo)


    def elenca_passeggeri(self):
        for i in self.lista_passeggeri:
            print(i)
