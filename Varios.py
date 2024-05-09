**************************************************************************************************************
import random
valor=random.randint(0,2)
lista=["Hola","Mundo","Guapo"]
print(lista[valor])



https://www.twitch.tv/docenteedctepantongo
https://github.com/Marquillos-99


**************************************************************************************************************
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



**************************************************************************************************************


class Vehiculo:
    def __init__(self,limite):
        self.velocidadlimite=limite
    def encender(self):
        print("El vehiculo encencio")
    def velocidadMax(self):
        print(self.velocidadlimite)

class Auto(Vehiculo):
    def __init__(self,marca,modelo,velocidad):
        super().__init__(velocidad)
        self.marca=marca
        self.modelo=modelo
    def quesoy(self):
        print("Soy un auto")
    
class Moto(Vehiculo):
    def __init__(self,marca,modelo,velocidad):
        self.marca=marca
        self.modelo=modelo
        super().__init__(velocidad)
    def quesoy(self):
        print("Soy una moto")

Pulsar=Moto("Honda","2020","300")
Tsuru=Auto("Nisan","2007","120")

Pulsar.encender()
Tsuru.encender()

Pulsar.velocidadMax()
Pulsar.quesoy()

Tsuru.velocidadMax()
Tsuru.quesoy()



************************************************************************************************************************
import random
valor=random.randint(1,10)
print(valor)

************************************************************************************************************************

class Series:
    def __init__(self,primo,factorial):
        self.prim=primo
        self.fact=factorial
        self.diccionario={}
        self.primosf()
        self.factorialf()
        self.imprimirDicc()
    def primosf(self):
        if self.prim <2:
            primo=False
        else:
            primo=True
        i=2
        while i<self.prim:
            if self.prim%i==0:
                i=self.prim
                primo=False
            i+=1
        self.diccionario['P_'+str(self.prim)]=primo
    def factorialf(self):
        acumulador=1
        for i in range(2,self.fact+1):
            acumulador*=i
        self.diccionario['F_'+str(self.fact)]=acumulador
    def imprimirDicc(self):
        print(self.diccionario)


obj=Series(5,5)

************************************************************************************************************************
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






************************************************************************************************************************

def primof(valor):
    if valor <2:
        primo=False
    else:
        primo=True
    i=2
    while i<valor:
        if valor%i==0:
            i=valor
            primo=False
        i+=1
    return primo
        
for i in range(0,18):
    print(i,primof(i))

************************************************************************************************************************
def factorial(num):
    acumulador=1
    for i in range(2,num+1):
        acumulador*=i
    return acumulador
pares=[]
impares=[]
for i in range(0,11):
    if i%2==0:
        pares.append(factorial(i))
    else:
        impares.append(factorial(i))
print(pares,"\n",impares)
************************************************************************************************************************
def factorial(num):
    acumulador=1
    for i in range(2,num+1):
        acumulador*=i
    return acumulador
    
print(factorial(5))

************************************************************************************************************************

def completo(nombre,apellido):
	return nombre+" "+apellido

nom=input("Digita tu nombre")
ape=input("Digita tu apellido")

print(completo(nom,ape))






************************************************************************************************************************
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

************************************************************************************************************************

for j in range(2,10+1):
    acumulado=1;
    for i in range(2,j+1):
        acumulado*=i
    print(acumulado)
************************************************************************************************************************
1
2
6
24
120
720
5040
40320

************************************************************************************************************************

valor=5
acumulado=1;
for i in range(2,valor+1):
    acumulado*=i
    
print(acumulado)

************************************************************************************************************************


lista=[]
for i in range(0,101):
	lista.append(i)
print(lista)

contador=0
while contador<=100:
	print(lista[contador],end=" ,")
	contador+=2

************************************************************************************************************************

diccionario={1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve",0:"cero"}
impares={}
for i in range(0,10):
	if i%2==0:
		print(i," - ",diccionario[i])
	else:
		impares[i]=diccionario[i]

print(impares)




************************************************************************************************************************



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



**************************************************************************************************************
class Pilares:
    def __init__(self,folios,nombres):
        self.lista_folios=folios
        self.lista_nombres=nombres
        self.diccionario={}
    def verFolios(self):
        for i in self.lista_folios:
            print(i)
    def verNombres(self):
        for i in self.lista_nombres:
            print(i)
    def genDicc(self):
        for i in range(0,len(self.lista_nombres)):
            self.diccionario[self.lista_nombres[i]]=self.lista_folios[i] 
        return self.diccionario


lista1=["123","456","789","547"]
lista2=["Luis","Ernesto","Maria","Dulce"]
PRDSM=Pilares(lista1,lista2)
print(PRDSM.genDicc())

PRDSM.verFolios()
PRDSM.verNombres()

        

**************************************************************************************************************


print("El animal ",Pato.sonido)

**************************************************************************************************************
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

**************************************************************************************************************
 [0, 2, 4, 6, 8, 10, 12, 14] 
 [1, 3, 5, 7, 9, 11, 13, 15] 
 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987] 
 {0: 'Par', 1: 'Impar', 2: 'Par', 3: 'Impar', 4: 'Par', 5: 'Impar', 6: 'Par', 7: 'Impar', 8: 'Par', 9: 'Impar', 10: 'Par', 11: 'Impar', 12: 'Par', 13: 'Impar', 14: 'Par', 15: 'Impar'} 

**************************************************************************************************************
meses={"1":"Enero","2":"FEEE","3":"Marzo","4":"Abril","5":"Mayo","6":"Junio","7":"Julio","8":"Agosto","9":"Septiembre","10":"Octubre","13":"Inexistente"}
print(meses)
meses["11"]="Noviembre"
meses["12"]="Diciembre"
meses["2"]="Febrero"
print(meses)
del meses["13"]
print(meses)


**************************************************************************************************************


meses={"1":"Enero","2":"Febrero","3":"Marzo","4":"Abril","5":"Mayo","6":"Junio","7":"Julio","8":"Agosto","9":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}
print(meses["1"])

**************************************************************************************************************
unatupla=("uno","dos","Tres")
print(unatupla)
tuplacambiada=list(unatupla)
print(tuplacambiada)


unalista=[1,2,3,4,[4.1,4.2]]
print(unalista)
unalistacambiada=tuple(unalista)
print(unalistacambiada)


******************************************************************************************
********************
pares=[]
impares=[]
for i in range(1,101):
	if i%2==0:
		pares.append(i)
	else:
		impares.append(i)
print(pares,"\n",impares)



**************************************************************************************************************
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
for m in meses:
	print(m)

**************************************************************************************************************

meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre"]
print(meses)
meses.append("Diciembre")
print(meses)
meses.insert(4, "MiMesInventado")
print(meses)
del meses[4]
print(meses)

**************************************************************************************************************

l=[22,True,"una lista",[1,2]]
print(l[0])
print(l[3])
print(l[3][0])

**************************************************************************************************************




































**************************************************************************************************************
def factorial(n):
    acum=1
    for i in range (1,n+1):
        acum=acum*i
    return acum

diccionario={}
for z in range(1,11):
    diccionario[z]=factorial(z)

print(diccionario)

**************************************************************************************************************
a=2
b=3
lista=[a,b]
print(lista[0])
print(lista[1])
print(lista[0]+lista[1])

**************************************************************************************************************
print("1.-Suma\n2.-Resta\n3.-Multiplicación\n4.-División")
opc=input("Digita la opción a realizar")
if(opc==1):
	#aqui empieza la suma
**************************************************************************************************************
class Coche:
    def __init__(self,gasolina):
        self.litros=gasolina
        print("Tenemos ", gasolina," litros")
    def arrancar(self):
        if self.litros>0:
            print("El auto encendio")
        else:
            print("El auto no arranca")
    def conducir(self):
        if self.litros>0:
            self.litros-=1
            print("Quedan ",self.litros," litros")
        else:
            print("No se mueve")
    def estatus(self):
        print("Tengo ",self.litros)

Tsuru=Coche(3)
Aveo=Coche(4)
Datsun=Coche(5)
print(Tsuru.litros," ",Aveo.litros )


Tsuru.arrancar()
Tsuru.conducir()
Tsuru.conducir()
Tsuru.conducir()
Tsuru.conducir()
Tsuru.conducir()



lista=[Tsuru,Aveo,Datsun]

for i in lista:
    i.estatus()
**************************************************************************************************************
def funcion():
    lista=[]
    num1=float(input("Digite el valor"))
    num2=float(input("Digite el valor"))
    lista.append(num1)
    lista.append(num2)
    return(lista[0]+lista[1])

******************************************************************************************************************
lista=[]
num1=float(input("Digite el valor"))
num2=float(input("Digite el valor"))
lista.append(num1)
lista.append(num2)
print(lista)
print(lista[0]+lista[1])
******************************************************************************************************************
class Coche:
    def __init__(self,gasolina):
        self.litros=gasolina
        print("Tenemos ", gasolina," litros")
    def arrancar(self):
        if self.litros>0:
            print("El auto encendio")
        else:
            print("El auto no arranca")
    def conducir(self):
        if self.litros>0:
            self.litros-=1
            print("Quedan ",self.litros," litros")
        else:
            print("No se mueve")


Tsuru=Coche(3)
Aveo=Coche(4)

print(Tsuru.litros," ",Aveo.litros )

Tsuru.arrancar()
Tsuru.conducir()
Tsuru.conducir()
Tsuru.conducir()
Tsuru.conducir()
Tsuru.conducir()
******************************************************************************************************************
def evaluar(x):
	if(x%2==0):
		validacion=True
	else:
		validacion=False
	return validacion

print("Inicio de mi programa")
for i in range(0,50):
	if(evaluar(i)):
		print(i)
******************************************************************************************************************
def suma(a,b):
	return (a+b)

print("Inicio de mi programa")
print(suma(2,3))

******************************************************************************************************************
def Saludar():
	return "Hola"
print("Inicio de mi programa")
print(Saludar())

******************************************************************************************************************
def pares(n):
	for i in range(0,n):
		if (i%2==0):
			print(i,end=",")
	print("")

print("Inicio de mi programa")
pares(100)


******************************************************************************************************************
def suma(x,y):
	print(x+y)

print("Bienvenido a las sumas")
suma(2,3)

******************************************************************************************************************
pares=[]
impares=[]
di={}
for i in range(0,51):
	if(i%2==0):
		pares.append(i)
		di[i]="PAR"
	else:
		impares.append(i)
		di[i]="IMPAR"

pares=tuple(pares)
impares=tuple(impares)
print(pares,"\n",impares,"\n",di)	



******************************************************************************************************************
nombres=["Luis","Ernesto","Mario","Ulises","Maria","Jose"]
numeros=["55123456789","5569657823","5535896254","5547496893","5511111111","55222222222"]
diccionario={}
i=0
while i< len(nombres):
	diccionario[nombres[i]]=numeros[i]
	i+=1
print(diccionario)

******************************************************************************************************************
diccionario={"Luis":[10,20,30],"Ernesto":"987654312"}
print(diccionario["Luis"][1])

******************************************************************************************************************
diccionario={"Luis":"123456789","Ernesto":"987654312"}
print(diccionario["Luis"])
diccionario["Luis"]="000000"
print(diccionario["Luis"])
diccionario["Mario"]="333333333"
print(diccionario)
del(diccionario["Luis"])
print(diccionario)

******************************************************************************************************************

def funcion():
    print("Hola")


print("Comienzo del programa")
funcion()


******************************************************************************************************************


meses={"1":"Enero","2":"Febrero","3":"Marzo","4":"Abril","5":"Mayo","6":"Junio","7":"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
print(meses[input("Digita un valor entre el 1 y el 12\n")])


******************************************************************************************************************
meses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
print(meses[int(input("Digita un valor entre el 1 y el 12\n"))])

mes=int(input("Digita un valor entre el 1 y el 12\n"))
print(meses[mes])

*************************************************************************************************
import random
nombres=("Luis","Ernesto","Jose","Maria","Juan")
apellidos=("Garcia","Sanchez","Perez","Sosa","Hernandez")
nombre_completo_1=[]
nombre_completo_2=[]
nombre_completo_3=[]
nombre_completo_1.append(nombres[random.randint(1,len(nombres)-1)])
nombre_completo_1.append(nombres[random.randint(1,len(nombres)-1)])

nombre_completo_1.append(apellidos[random.randint(1,len(apellidos)-1)])
nombre_completo_1.append(apellidos[random.randint(1,len(apellidos)-1)])
print(nombre_completo_1,"\n",nombre_completo_2,"\n",nombre_completo_3)





******************************************************************************************************
caracter_a_letra={"1":"uno","2":"dos","3":"tres","4":"cuatro","5":"cinco"}
num_a_letra={1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco"}

print(caracter_a_letra["1"])
print(num_a_letra[2])

for i in caracter_a_letra:
    print(i," ",caracter_a_letra[i])

print("")

for i in num_a_letra:
    print(i," ",num_a_letra[i])

***************************************************
import random
print(random.randint(0,10))
****************************************************
tupla = ("Manzana", "Fresa", "Frambueza")
print(tupla)
lista=list(tupla)
lista.append("Pera")
tupla=tuple(lista)
print(tupla)



****************************************************
tupla = ("Manzana", "Fresa", "Frambueza")
print(tupla)
print(tupla[1])
for i in tupla:
    print(i)

l=len(tupla)
i=0
print(l)
while i<l:
    print(tupla[i])
    i+=1



****************************************************

variable=0
while variable<10:
    print(variable)
    variable+=1 #esto es lo mismo que variable=variable+1
print("Fin del programa")

****************************************************

print("Hola")

****************************************************

c=input("Digita un num")
b=float(c)



b=float(input("Digita el número"))

****************************************************

b=input("Digita un número\n")
bentero=float(b)
if bentero>0:
    print("Es positivo")
    if bentero%2==0:
        print("Es par")
print("Sigue el flujo")

****************************************************
for i in range (10,20):
    print("X")
    print(i)
	

for i in range(5):
    print(i, end=", ")

****************************************************

b=input("Digita un número\n")
bentero=float(b)
if bentero>0:
    print("Es positivo")
elif(bentero<0):
    print("Es negativo")
else:
    print("Es cero")

********************************************
lista=["uno","dos","tres","cuatro","cinco","seis","siete"]
print(lista[0])
print(lista[5])

for valor in lista:
    print(valor)

********************************************

lista1=["uno","dos","tres","cuatro","cinco","seis","siete"]
lista2=[True,4,"Hola",[1,2]]


lista1.append("ocho")
lista2.extend([3, 4])

for valor in lista1:
    print(valor,end=" ")
print("")
for valor in lista2:
    print(valor,end=" ")


print("\n",lista2[3][0])

********************************************
del lista1[1]
print("")
for valor in lista1:
    print(valor,end=", ")
print("")

********************************************
lista1.insert(4, "mi lista")
print("")
for valor in lista1:
    print(valor,end=", ")
print("")

*****************************************
lista=[]
for i in range(0,20):
    if i%2==0:
        lista.append(i)
print(lista)

***********************************
n=[5,8,79,6,7,4,7,89,6,2,1,52,6,8,7,1,2,6,8,7,3,6,9,7,74,1,2,55,66,33,35,36,98,65,74,15,21,23]


**********************************
n=[5,8,79,6,7,4,7,89,6,2,1,52,6,8,7,1,2,6,8,7,3,6,9,7,74,1,2,55,66,33,35,36,98,65,74,15,21,23]
for i in range(len(n)):
    for j in range(1,len(n)):
        if n[j]<n[j-1]:
            temp=n[j-1]
            n[j-1]=n[j]
            n[j]=temp
print(n)
