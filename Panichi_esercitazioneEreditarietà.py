class Veicolo:
    def __init__(self, codice, marca, modello, prezzo, annoRevisione):
        self.codice = codice
        self.marca = marca
        self.modello = modello
        self.prezzo = prezzo
        self.annoRevisione = annoRevisione

    def scheda_veicolo(self):
        return f"Codice: {self.codice}; Marca: {self.marca}; Modello: {self.modello}; Prezzo: {self.prezzo}; Anno di revisione: {self.annoRevisione}"


    def modifica_scheda(self):
        self.codice = input("Inserisci il nuovo codice: ")
        self.marca = input("Inserisci la nuova marca: ")
        self.modello = input("Inserisci il nuovo modello: ")
        self.prezzo = float(input("Inserisci il nuovo prezzo: "))
        self.annoRevisione = int(input("Inserisci il nuovo anno di revisione: "))
        print("Modifica effettuata con successo.")


class Automobile(Veicolo):
    def __init__(self, codice, marca, modello, prezzo, annoRevisione, lunghezza, larghezza):
        super().__init__(codice, marca, modello, prezzo, annoRevisione)
        self.lunghezza = lunghezza
        self.larghezza = larghezza

    def scheda_veicolo(self):
        return f"{super().scheda_veicolo()}; Lunghezza: {self.lunghezza}; Larghezza: {self.larghezza}\n"


class Motociclo(Veicolo):
    def __init__(self, codice, marca, modello, prezzo, annoRevisione, tipo, potenza):
        super().__init__(codice, marca, modello, prezzo, annoRevisione)
        self.tipo = tipo
        self.potenza = potenza

    def scheda_veicolo(self):
        return f"{super().scheda_veicolo()}; Tipo: {self.tipo}; Potenza: {self.potenza}\n"


class Vendita:
    def __init__(self, codice, data, codiceVenditore):
        self.codice = codice
        self.data = data
        self.codiceVenditore = codiceVenditore
        self.automobili = []
        self.motocicli = []

    def aggiungi_veicolo(self, veicolo):
        if isinstance(veicolo, Automobile):
            self.automobili.append(veicolo)
            print("Automobile aggiunta con successo")
        elif isinstance(veicolo, Motociclo):
            self.motocicli.append(veicolo)
            print("Motociclo aggiunto con successo")
        else:
            print("Errore in aggiunta")

    def rimuovi_veicolo(self, veicolo):
        if isinstance(veicolo, Automobile):
            self.automobili.remove(veicolo)
            print("Automobile rimossa con successo")
        elif isinstance(veicolo, Motociclo):
            self.motocicli.remove(veicolo)
            print("Motociclo rimosso con successo")
        else:
            print("Errore non presente")

    def importo_vendita(self):
        guadagno = 0
        tot = len(self.automobili) + len(self.motocicli)
        print(f"I veicoli presenti sono {tot}")
        for veicolo in self.automobili:
            guadagno += veicolo.prezzo
        for veicolo in self.motocicli:
            guadagno += veicolo.prezzo
        print(f"Guadagno totale: {guadagno}")
        return guadagno

    def dettaglio_vendita(self):
        somma_auto = 0
        somma_moto = 0

        for auto in self.automobili:
            somma_auto += auto.prezzo
        for moto in self.motocicli:
            somma_moto += moto.prezzo

        provvigione_auto = somma_auto * 0.03  
        provvigione_moto = somma_moto * 0.02  
        totale_provvigione = provvigione_auto + provvigione_moto

        somma_totale = somma_auto + somma_moto

        print(f"Somma automobili: {somma_auto}")
        print(f"Somma motocicli: {somma_moto}")
        print(f"Somma totale veicoli: {somma_totale}")
        print(f"Provvigione totale: {totale_provvigione}")

        return [somma_auto, somma_moto, somma_totale, totale_provvigione]


a2 = Automobile(2,"Peugeot","Peugeot 2008",18000,2014,4.2,1.75)
m1 = Motociclo(3,"Gilera","Gilera Runner 50",3500,2016,"Scooter",1200)
m2 = Motociclo(4,"Honda","SW-T 400 – 2013",4500,2012,"Super Sport",1000)

vendita1=Vendita(1,"01/04/2022",'123')
vendita1.aggiungi_veicolo(a2)
vendita1.aggiungi_veicolo(m1)
vendita1.aggiungi_veicolo(m2)

vendita1.rimuovi_veicolo(m2)

vendita1.importo_vendita()

importi=vendita1.dettaglio_vendita()
print("--------------------------")
print(f"\nImporto Automobili= {importi[0]}")
print(f"\nImporto Motocicli= {importi[1]}")
print(f"\nImporto Totale= {importi[2]}")
print(f"\nImporto Provvigione= {importi[3]}")

class Vendite():
  def __init__(self,nome_negozio,codice_negozio):
    self.nome_negozio=nome_negozio
    self.codice_negozio=codice_negozio
    self.vendite=[]

  def aggiungi_vendita(self,vendita):
    self.vendite.append(vendita)


  def rimuovi_vendita(self,vendita):
    self.vendite.remove(vendita)


  def totale_vendite(self):
    totA=0
    totM=0
    for vendita in self.vendite:
      for auto in vendita.automobili:
        totA += auto.prezzo
      for moto in vendita.motocicli:
        totM += moto.prezzo
    return ([totA,totM,totA+totM])
  
vendite_negozio=Vendite("Concessionaria Magenta ",1)
vendite_negozio.aggiungi_vendita(vendita1)
vendite_negozio.rimuovi_vendita(vendita1)

vendite_negozio.aggiungi_vendita(vendita1)

a3 = Automobile(5,"Renault","Renault Clio",12000,2020,3.2,1.55)

m3 =  Motociclo(6,"Honda","SW-T 500",5500,2021,"Sport",1200)
vendita2=Vendita(2,"2/04/2022",'234')
vendita2.aggiungi_veicolo(a3)
vendita2.aggiungi_veicolo(m3)

vendite_negozio.aggiungi_vendita(vendita2)

importiTotali=vendite_negozio.totale_vendite()
print("--------------------------")
print(f"\nImporto totale automobili= {importiTotali[0]}")
print(f"\nImporto totale motocilci= {importiTotali[1]}")
print(f"\nImporto totale di tutte le vendite= {importiTotali[2]}")
