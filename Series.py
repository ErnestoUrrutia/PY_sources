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