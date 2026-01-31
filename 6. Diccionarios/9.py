facturas, cobrado = {}, 0

while True:
	print("\n--- Gestión de Facturas ---")
	print("1. Añadir factura")
	print("2. Pagar factura")
	print("3. Salir")
	
	opcion = input("Elige una opción (1-3): ").strip()
	
	if opcion == "1":
		num_factura = input("Número de factura: ").strip()
		try:
			coste = float(input("Coste de la factura: "))
			if coste > 0:
				facturas[num_factura] = coste; print(f"Factura {num_factura} añadida correctamente.")
			else:
				print("El coste debe ser positivo.")
		except ValueError:
			print("Coste inválido.")
	
	elif opcion == "2":
		num_factura = input("Número de factura a pagar: ").strip()
		if num_factura in facturas:
			cobrado += facturas[num_factura]
			del facturas[num_factura]; print(f"Factura {num_factura} pagada correctamente.")
		else:
			print("Factura no encontrada.")
	
	elif opcion == "3":
		print("¡Hasta luego!"); break
	
	else:
		print("Opción inválida."); continue

	pendiente = sum(facturas.values())
	print(f"\nCobrado: {cobrado:.2f}€")
	print(f"Pendiente: {pendiente:.2f}€")