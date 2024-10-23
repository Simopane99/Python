#Svolto senza l'utilizzo delle risorse
class Articolo:#9:25
  def __init__(self, codice, fornitore, marca,prezzo, quantita):
    self.codice=codice
    self.fornitore=fornitore
    self.marca=marca
    self.prezzo=prezzo
    self.quantita=quantita

  def scheda_articolo(self):
    return f"\nCodice: {self.codice};\nFornitore: {self.fornitore};\nMarca: {self.marca};\nPrezzo: {self.prezzo};\nQuantità: {self.quantita}\n"
  
  def modifica_scheda(self):
    print(f"\n-1 Fornitore: {self.fornitore};\n-2 Marca: {self.marca};\n-3 Prezzo: {self.prezzo};\n-4 Quantità: {self.quantita}\n")
    scelta=int(input("Quale desideri modificare? "))
    if(scelta==1):
      self.fornitore= input("Inserisci il nuovo fornitore")
    elif(scelta==2):
      self.marca = input("Inserisci la nuova marca: ")
    elif(scelta==3):
      self.prezzo = float(input("Inserisci il nuovo prezzo: "))
      while(self.prezzo<0):
        self.prezzo = float(input("Inserisci il nuovo prezzo: "))
    elif(scelta==4):  
      self.quantita = int(input("Inserisci la nuova quantità: "))
      while(self.quantita<1):
        self.quantita = int(input("Inserisci la nuova quantità: "))

class Televisore(Articolo):#9:30
    def __init__(self, codice, fornitore,marca,prezzo,quantita,pollici,tipo):
      super().__init__(codice,fornitore,marca,prezzo,quantita)
      self.pollici=pollici
      self.tipo=tipo

    def scheda_articolo(self):
      return f"{super().scheda_articolo()}Pollici: {self.pollici}\nTipo: {self.tipo}\n"

class Frigorifero(Articolo):#9:36
  def __init__(self, codice, fornitore, marca, prezzo, quantita,dimensioni,modello):
    super().__init__(codice, fornitore, marca,prezzo, quantita)
    self.dimensioni=dimensioni
    self.modello=modello

  def scheda_articolo(self):
    return f"{super().scheda_articolo()}Dimensioni: {self.dimensioni}\nModello: {self.modello}\n"

t1 = Televisore(1,"Fornitore 1","Sony",700,10,40,"Schermo piatto")
print(t1.scheda_articolo())
t1.modifica_scheda()
print(t1.scheda_articolo())

class Ordine():#9:46
  def __init__(self,codice,data, piva,indirizzo):
    self.codice=codice
    self.data=data
    self.piva=piva
    self.indirizzo=indirizzo
    self.articoli=[]

  def aggiungi_articolo(self,articolo):
    if isinstance(articolo,Televisore):
      self.articoli.append(articolo)
      print("Televisore aggiunto")
    elif isinstance(articolo,Frigorifero):
      self.articoli.append(articolo)
      print("Frigorifero aggiunto")
    

  def rimuovi_articolo(self,articolo):
    if articolo in self.articoli:
      self.articoli.remove(articolo)


  def importo_ordine(self):
    print(f"Gli articoli presenti sono {len(self.articoli)}")
    for articolo in self.articoli:
      p=articolo.prezzo
      q=articolo.quantita
      print(f"{articolo.marca} ha un importo di {(p*q):.2f}")

  def dettaglio_ordine(self):
    sommaT=0; sommaF=0

    for articolo in self.articoli:
      importo=articolo.prezzo*articolo.quantita
      if isinstance(articolo,Televisore):
        print(f"\nArticolo: televisore")
        sommaT+=importo

      if isinstance(articolo,Frigorifero):
        print(f"\nArticolo: frigorifero")
        sommaF+=importo

      print(f"Importo= {importo}\n{articolo.scheda_articolo()}")
    
    print(f"\nImporto totale: {sommaF+sommaT}")
    
    return([sommaT,sommaF,sommaT+sommaF])
  
t2 = Televisore(2,"Fornitore 2","Samsung",1000,5,80,"Schermo curvo")
f1 = Frigorifero(3,"Fornitore 3","Bosch",750,12,'790x2000x600','Ultra')
f2 = Frigorifero(4,"Fornitore 4","Ariston",550,10,'590x1600x500','Medium')

ordine1=Ordine(1,"24/02/2022",'213143','Via della consegna 1')
ordine1.aggiungi_articolo(t2)
ordine1.aggiungi_articolo(f1)
ordine1.aggiungi_articolo(f2)

ordine1.rimuovi_articolo(f2)

ordine1.importo_ordine()

importi=ordine1.dettaglio_ordine()
print("--------------------------")
print(f"\nImporto televisori= {importi[0]}")
print(f"\nImporto frigoriferi= {importi[1]}")
print(f"\nImporto totale= {importi[2]}")

class Ordini():#10:36
  def __init__(self,nome_negozio,codice_negozio):
    self.nome_negozio=nome_negozio
    self.codice_negozio=codice_negozio
    self.ordini=[]

  def aggiungi_ordine(self,ordine):
    self.ordini.append(ordine)
    print("Ordine aggiunto con successo")

  def rimuovi_ordine(self,ordine):
    if(ordine in self.ordini):
      self.ordini.remove(ordine)

  def totale_ordini(self):
    sommaT=0; sommaF=0
    for ordine in self.ordini:
      for articolo in ordine.articoli:
        importo=articolo.prezzo*articolo.quantita
        if isinstance(articolo,Televisore):
          sommaT+=importo

        if isinstance(articolo,Frigorifero):
          sommaF+=importo

    return ([sommaT,sommaF,sommaF+sommaT])
  
ordini_negozio=Ordini("Megastore vendita ",1)
ordini_negozio.aggiungi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)
ordini_negozio.rimuovi_ordine(ordine1)

ordini_negozio.aggiungi_ordine(ordine1)

t3 = Televisore(5,"Fornitore 5","LG",600,4,70,"Schermo curvo")
f3 = Frigorifero(6,"Fornitore 6","Bosch",450,10,'490x1000x400','Small')
ordine2=Ordine(2,"25/02/2022",'213113','Via della consegna 2')
ordine2.aggiungi_articolo(t3)
ordine2.aggiungi_articolo(f3)

ordini_negozio.aggiungi_ordine(ordine2)

importiTotali=ordini_negozio.totale_ordini()
print("--------------------------")
print(f"\nImporto totale televisori= {importiTotali[0]}")
print(f"\nImporto totale frigoriferi= {importiTotali[1]}")
print(f"\nImporto totale tutti gli ordini= {importiTotali[2]}")

