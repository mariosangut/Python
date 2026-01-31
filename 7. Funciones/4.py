def calcular_total_factura(cantidad, iva=21):
	return cantidad * (1 + iva / 100)

print(calcular_total_factura(100)) 