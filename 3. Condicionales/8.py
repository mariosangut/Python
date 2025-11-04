trabajador = float(input("Introduce tu puntuación: "))

if trabajador == 0.0:
    nivel = "Inaceptable"
elif trabajador == 0.4:
    nivel = "Aceptable"
elif trabajador >= 0.6:
    nivel = "Metiorito"

print (f"El nivel de rendimiento obtenido es: {nivel}, y el dinero que recibirá será {2400*trabajador + 2400} €")