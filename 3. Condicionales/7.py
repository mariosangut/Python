renta=int(input("Ingrese el valor de la renta anual: "))

if renta < 10000:
    impuesto = 0.05
elif renta >= 10000 and renta <= 20000:
    impuesto = 0.15
elif renta >= 20000 and renta <= 35000:
    impuesto = 0.2
elif renta >= 35000 and renta <= 60000:
    impuesto = 0,3
elif renta > 60000:
    impuesto = 0.45

print (f"Te corresponde el siguiente impostivo: {impuesto}%")
