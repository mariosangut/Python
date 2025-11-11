numero = int(input("Introduce un numero entero positivo: "))
x = 1

while x<numero:
    if (x %2 != 0 and x<numero-1):
        print (x, end=",") 
    elif (x %2 != 0 ):
        print (x)
    
    x+=1

print ()