

class Auto:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        
    
    def descrizione(self, velocita):
        
        return f"Auto: {self.marca} {self.modello}, Anno: {self.anno}, Velocità fissa: {velocita}"

    def aumentaVelocita(self, incremento, velocita):
        
        velocita += incremento
        return f"Velocità aumentata di {incremento} km/h. Velocità attuale: {velocita} km/h"
        

    def diminuisciVelocita(self, decremento,velocita):
       
        velocita -= decremento 
        return f"Velocità diminuita di {decremento} km/h. Velocità attuale: {velocita} km/h"
