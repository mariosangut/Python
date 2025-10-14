edad = int(input("Introduce tu edad: "))
ingresos = int(input("Introduce tus ingresos mensuales: "))

if edad > 16 and ingresos >= 1000:
    print("El usuario tiene que tributar")
else:
    print("El usuario no tiene que tributar")
