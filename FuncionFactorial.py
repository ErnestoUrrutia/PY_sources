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


def factorial(num):
    acumulador=1
    for i in range(2,num+1):
        acumulador*=i
    return acumulador
    
print(factorial(5))