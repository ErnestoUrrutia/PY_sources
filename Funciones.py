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