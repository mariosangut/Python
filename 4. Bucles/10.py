num = int(input("Introduce un numero: "))
i = 1
contador = 0

while i <= num : 
    if num % i == 0:
        contador += 1
    i = i + 1
        
if contador == 2 :
    print (f"El numero {num} es primo")
else :
    print (f"El numero {num} NO es primo")