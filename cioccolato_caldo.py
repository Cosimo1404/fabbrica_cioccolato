# cioccolato_caldo.py

from main import Cioccolato

class CioccolatoCaldo(Cioccolato):
    def __init__(self, tipo, percentuale_cacao, temperatura, densita):
        super().__init__(tipo, percentuale_cacao)
        self.temperatura = temperatura  # temperatura della bevanda
        self.densita = densita  # densità del cioccolato caldo

    def produce(self):
        super().produce()
        print(f"Temperatura: {self.temperatura}°C, Densità: {self.densita}g/ml")

# Esempio di utilizzo della classe CioccolatoCaldo
if __name__ == "__main__":
    cioccolato_caldo = CioccolatoCaldo("Bianco", 30, 75, 1.2)
    cioccolato_caldo.produce()
