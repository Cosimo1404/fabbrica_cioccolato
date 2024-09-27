# tavolette.py

from main import Cioccolato

class Tavoletta(Cioccolato):
    def __init__(self, tipo, percentuale_cacao, peso, ha_aggiunte):
        super().__init__(tipo, percentuale_cacao)
        self.peso = peso  # peso della tavoletta
        self.ha_aggiunte = ha_aggiunte  # se contiene aggiunte

    def produce(self):
        super().produce()
        aggiunta = "con aggiunte" if self.ha_aggiunte else "senza aggiunte"
        print(f"Peso: {self.peso}g, {aggiunta}")

# Esempio di utilizzo della classe Tavoletta
if __name__ == "__main__":
    tavoletta = Tavoletta("Fondente", 80, 100, True)
    tavoletta.produce()
