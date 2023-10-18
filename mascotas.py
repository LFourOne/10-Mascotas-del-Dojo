class Mascota:
    def __init__(self, nombre, tipo, golosinas, salud, energia):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia
    def dormir(self):
        self.energia += 25
    def comer(self):
        self.energia += 5
        self.salud += 10
    def jugar(self):
        self.salud += 5
    def sonido(self):
        print("¡Guau! ¡Guau!")

