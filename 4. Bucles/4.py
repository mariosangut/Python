numero = int(input("Introduce un numero entero positivo: "))

final = 0
for x in range(numero, final, -1):
        if x>final+1:
            print (x, end=",")
        elif x>final:
            print (x)
print ()