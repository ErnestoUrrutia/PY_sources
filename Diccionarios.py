diccionario={1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve",0:"cero"}
impares={}
for i in range(0,10):
	if i%2==0:
		print(i," - ",diccionario[i])
	else:
		impares[i]=diccionario[i]

print(impares)
