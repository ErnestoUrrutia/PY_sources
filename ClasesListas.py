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