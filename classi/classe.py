# class Persona:
#     specie= "Homo sapiens" # Attributo di classe
    
#     def __init__(self, nome, eta):
#         self.nome = nome 
#         self.eta = eta

# persona1 = Persona("Mario", 30)
# print(persona1.specie)
# print(persona1.nome)


class Persona:
    def saluta(self):
        print("Ciao")

class Studente(Persona):
    def saluta(self):
        print("Ciao, sono un negro")
        
persona1 = Persona()
studente1 = Studente()
persona1.saluta()
studente1.saluta()