class Persona:
	def __init__(self,nombre,edad):
		self.miNombre=nombre
		self.miEdad=edad
	def Presentarme(self):
		print("Mi nombre es: ",self.miNombre)
	def DecirEdad(self):
		print("Mi edad es: ",self.miEdad)

Maestro=Persona("Luis",20)
Estudiante=Persona("Maria",25)


Maestro.Presentarme()
Estudiante.Presentarme()

Maestro.DecirEdad()
Estudiante.DecirEdad()


print(Maestro.miNombre)
print(Estudiante.miNombre)
