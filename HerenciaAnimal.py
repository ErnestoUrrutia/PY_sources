
class Animal:
    def __init__(self,habitat,alimentacion):
        self.habitat=habitat
        self.alimentacion=alimentacion

    def viveEn(self):
        print("El vive en: ",self.habitat)
    def come(self):
        print("El come: ",self.alimentacion)

class Perros(Animal):
    def __init__(self,nombre,edad):
        super().__init__("Domestico","Sobras")
        self.nombre=nombre
        self.edad=edad
    def mellamo(self):
        print("Mi nombre es: ",self.nombre)
    def tengoEdad(self):
        print("Mi edad es: ",self.edad)


class Gatos(Animal):
    def __init__(self,nombre,edad):
        super().__init__("Domestico/Callejero","Sobresitos")
        self.nombre=nombre
        self.edad=edad
    def mellamo(self):
        print("Mi nombre es: ",self.nombre)
    def tengoEdad(self):
        print("Mi edad es: ",self.edad)


Egipcio=Gatos("Kratos",5)

PastorAleman=Perros("Firulais",3)


Egipcio.mellamo()
PastorAleman.mellamo()

Egipcio.tengoEdad()
PastorAleman.tengoEdad()


Egipcio.viveEn()
PastorAleman.viveEn()

Egipcio.come()
PastorAleman.come()
