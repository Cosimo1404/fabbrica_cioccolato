
# main.py

class Cioccolato:
    def __init__(self, tipo, percentuale_cacao):
        self.tipo = tipo  # tipo di cioccolato (fondente, al latte, bianco)
        self.percentuale_cacao = percentuale_cacao  # percentuale di cacao
        self.MAX_PRODUZIONE = 100  # produzione massima al giorno

    def produce(self):
        print(f"Produzione di cioccolato {self.tipo} con {self.percentuale_cacao}% di cacao.")

# Esempio di utilizzo della classe base
if __name__ == "__main__":
    cioccolato = Cioccolato("Fondente", 70)
    cioccolato.produce()
