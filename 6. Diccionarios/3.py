precios = {
	'Manzana': .8,
	'Pera': .85,
	'Naranja': .7,
	'Plátano': 1.35
}

fruta = input("Ingrese el nombre de la fruta (Manzana, Pera, Naranja, Plátano): ")
if fruta in precios:
	kilos = float(input("Ingrese la cantidad de kilos: "))
	total = precios[fruta] * kilos
	print(f"El precio total de {kilos} kg de {fruta} es: {total:.2f} euros")
else:
	print("Fruta no disponible")

