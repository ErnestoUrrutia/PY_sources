def suma(a,b):
	return a+b

x=int(input("Digita el primer valor\n"))
y=int(input("Digita el segundo valor\n"))

print("El resultado es:",suma(x,y))

************************************************************************************************************************
def suma(a,b):
	print("El resultado es: ",a+b)

x=int(input("Digita el primer valor\n"))
y=int(input("Digita el segundo valor\n"))

suma(x,y)



************************************************************************************************************************
def saludar(nombre):
	print("Hola ",nombre)
def despedir(nombre):
	print("Adios ",nombre)

soy=input("Digita tu nombre\n")
saludar("Luis")
despedir("Luis")