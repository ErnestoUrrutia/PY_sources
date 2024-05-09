class Animal:
    def hablar(self):
        print("Ruido")


class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

firu=Perro()
firu.hablar()