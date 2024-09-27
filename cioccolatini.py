# cioccolatini.py

from main import Cioccolato

class Cioccolatino(Cioccolato):
    def __init__(self, tipo, percentuale_cacao, forma, ripieno):
        super().__init__(tipo, percentuale_cacao)
        self.forma = forma  # forma del cioccolatino
        self.ripieno = ripieno  # ripieno del cioccolatino

    def produce(self):
        super().produce()
        print(f"Forma: {self.forma}, Ripieno: {self.ripieno}")

# Esempio di utilizzo della classe Cioccolatino
if __name__ == "__main__":
    cioccolatino = Cioccolatino("Al Latte", 50, "Cuore", "Crema di Nocciola")
    cioccolatino.produce()
