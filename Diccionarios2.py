meses={"1":"Enero","2":"FEEE","3":"Marzo","4":"Abril","5":"Mayo","6":"Junio","7":"Julio","8":"Agosto","9":"Septiembre","10":"Octubre","13":"Inexistente"}
print(meses)
meses["11"]="Noviembre"
meses["12"]="Diciembre"
meses["2"]="Febrero"
print(meses)
del meses["13"]
print(meses)