from cabina import Cabina,Deluxe,CabinaAnimali
from passeggero import Passeggero
from prenotazione import Prenotazione
class Crociera:
    def __init__(self, nome):
        self._nome = nome
        self.lista_passeggeri= []
        self.lista_cabine = []
        self.lista_prenotazioni= []

    ##utilizzo i metodi getter e setter per il cambio del nome

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
                    if len(riga)==5 and not riga[4].isdigit(): ##verifico appartenenza classe cabina Deluxe
                        codice, numero_letti, numero_ponte, prezzo,tipologia = riga
                        new_cabina = Deluxe(codice,numero_letti,numero_ponte,prezzo,tipologia)
                        cabine.append(new_cabina)
                    elif len(riga)==3:  ##verifico appartenenza classe passeggero
                        codice_univoco,nome,cognome= riga
                        new_passeggero = Passeggero(codice_univoco,nome,cognome)
                        passeggeri.append(new_passeggero)
                    elif len(riga) == 4: ##verifico appartenenza classe standard
                        codice, numero_letti, numero_ponte, prezzo = riga
                        new_cabina = Cabina(codice,numero_letti,numero_ponte,prezzo)
                        cabine.append(new_cabina)
                    elif len(riga) == 5 and riga[4].isdigit(): ##verifico appartenenza classe cabinaAnimali
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
            if i.numero_univoco == codice_passeggero:  ##verifico che passeggero esista
                condizione = True
        for i in self.lista_cabine:
            if i.codice == codice_cabina:   ##verifico che cabina esista
                condizione2 = True
        for i in self.lista_cabine:
            if not i.disponibile:       ##verifico che la cabina sia disponibile usando
                condizione3 = False      ##l'attributo di classe disponibilità
        for i in prenotazioni:
            if i.codice_passeggero == codice_passeggero:   ##verifico che il passeggero non abbia
                condizione4= False                        ##un'altra cabina assegnata
        ##se una delle 4 condizioni non è soddisfatta il metodo solleva un eccezione
        if condizione==False or condizione2==False or condizione3==False or condizione4==False:
            raise Exception("eccezione: la cabina non esiste o il passeggero non esiste o cabina già assegnata o passeggero già fornito di cabina")
        ##in caso contrario la prenotazione può avvenire
        else:
            elemento = None
            elemento2= None
            prenotazione = Prenotazione(codice_cabina,codice_passeggero)
            prenotazioni.append(prenotazione)
            for i in self.lista_passeggeri:
                if i.numero_univoco == codice_passeggero:
                    elemento2 = i      ##in questo modo preparo già la struttura dati
                else:                 ##per il punto 5 andando ad aggiungere come attributo di classe
                    pass           ##tramite il metodo associa_cabina il codice della cabina al passeggero
            if elemento2 is not None:
                elemento2.assegna_cabina(codice_cabina)

            for i in self.lista_cabine:
                if i.codice == codice_cabina:
                    elemento = i                ##utilizzo metodo disponibilità per aggiornare
                else:                           ##lo stato della cabina
                    pass
            if elemento is not None:
                elemento.disponibilità()

    def cabine_ordinate_per_prezzo(self):
        for i in self.lista_cabine:               ##dopo aver richiamato il metodo calcolo_prezzo diverso per ogni tipo di cabina
            i.calcolo_prezzo()                     ##utilizzo lambda expression per ordinare la lista delle cabine
        return sorted(self.lista_cabine,key=lambda s: s.prezzo)   ##in base al prezzo


    def elenca_passeggeri(self):
        for i in self.lista_passeggeri:
            print(i)
