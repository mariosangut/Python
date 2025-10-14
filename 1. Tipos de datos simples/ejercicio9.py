capital = float(input("Introduce el importe capital: "))
interes = float(input("Introduce el interes: "))
tiempo = float(input("Introduce el timepo en años: "))

resultado = capital * (interes/100) * tiempo
print(f"El dinero es {resultado}")

