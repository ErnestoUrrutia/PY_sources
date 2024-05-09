class Animal:
    def __init__(self,sonido,n_patas):
        self.sonido=sonido
        self.n_patas=n_patas
    def comunicar(self):
        return self.sonido
    def caminar(self):
        if self.n_patas==4:
            return "Cuadrupedo"
        else:
            return "Bipedo"

Pato=Animal("Grazna",2)
Gato=Animal("Maulla",4)
Perro=Animal("Ladra",4)


print("El animal es: ",Pato.caminar())
print("El animal ",Pato.comunicar())


print("El animal es: ",Gato.caminar())
print("El animal ",Gato.comunicar())



print("El animal es: ",Perro.caminar())
print("El animal ",Perro.comunicar())