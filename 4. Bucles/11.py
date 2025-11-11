palabra = input("Introduce una palabra: ")
longitudPalabra = len(palabra)

for i in range (longitudPalabra -1, -1, -1):
        print (palabra[i], end=" ")
print ()