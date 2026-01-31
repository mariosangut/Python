cesta, total = {}, 0

print("=== CESTA DE COMPRA ===\n")

while True:
	articulo = input("Ingrese el artículo (o 'salir' para terminar): ").strip()
	if articulo.lower() == 'salir': break
	
	try:
		precio = float(input(f"Ingrese el precio de {articulo}: "))
		
		if articulo in cesta: cesta[articulo] += precio
		else: cesta[articulo] = precio
		
		print(f"✓ {articulo} añadido a la cesta\n")
	
	except ValueError:
		print("⚠ Error: Ingrese un precio válido\n")

print("\n" + "="*40)
print("LISTA DE COMPRA")
print("="*40)

for articulo, precio in cesta.items():
	print(f"{articulo:<25} ${precio:>8.2f}")

total = sum(cesta.values())
print("="*40)
print(f"{'TOTAL':<25} ${total:>8.2f}")
print("="*40)