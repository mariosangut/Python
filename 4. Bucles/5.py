capital = float(input("Introduce la cantidad que vas a invertir: "))
tasaInteres = float(input("Interés anual (en %): ")) / 100
años = int(input("¿Cuántos años va a estar invertido?: "))

x = 1
while x <= años:
    capital *= (1 + tasaInteres)  # Aplica el interés una vez por año
    print(f"El capital obtenido al final del año {x} sería de {capital:.2f} €")
    x += 1
