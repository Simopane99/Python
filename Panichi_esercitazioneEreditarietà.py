class Veicolo:
  def __init__(self, codice, marca, modello,prezzo, annoRevisione):
    self.codice=codice
    self.marca=marca
    self.modello=modello
    self.prezzo=prezzo
    self.annoRevisione=annoRevisione

  def scheda_veicolo(self):
    return f"Codice: {self.codice}; Marca: {self.marca}; Modello: {self.modello}; Prezzo: {self.prezzo}; Anno di revisione: {self.annoRevisione}\n"


  def modifica_scheda(self):
    self.codice = input("Inserisci il nuovo codice: ")
    self.marca = input("Inserisci la nuova marca: ")
    self.modello = int(input("Inserisci il nuovo modello: "))
    self.prezzo = input("Inserisci il nuovo prezzo: ")
    self.annoRevisione = input("Inserisci il nuovo anno di revisione: ")
    print("Modifica effettuata con successo.")

class Automobile(Veicolo):
    def __init__(self, codice, marca, modello,prezzo, annoRevisione,lunghezza,larghezza):
        super().__init__(codice, marca, modello,prezzo, annoRevisione)
        self.lunghezza=lunghezza
        self.larghezza=larghezza

    def scheda_veicolo(self):
      return f"{super().scheda_veicolo()} Lunghezza: {self.lunghezza}; Larghezza: {self.larghezza}\n"

class Motociclo(Veicolo):
  def __init__(self, codice, marca, modello,prezzo, annoRevisione,tipo,potenza):
    super().__init__(codice, marca, modello,prezzo, annoRevisione)
    self.tipo=tipo
    self.potenza=potenza

  def scheda_veicolo(self):
    return f"{super().scheda_veicolo()} Tipo: {self.tipo}; Potenza: {self.potenza}\n"
