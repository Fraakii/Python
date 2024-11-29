from ClasseAuto import Auto

velocita = 50
# Creazione di un oggetto della classe Auto
macchina1 = Auto(marca="Fiat", modello="Panda", anno=2020)

# Descrizione iniziale dell'auto
print(macchina1.descrizione(velocita))

# Aumento della velocità
incremento = 20
print(macchina1.aumentaVelocita(incremento, velocita))

# Diminuzione della velocità
decremento = 30
print(macchina1.diminuisciVelocita(decremento,velocita))

