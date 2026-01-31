persona = {}

while True:
	clave = input("Ingrese la clave del dato (o 'salir' para terminar): ")	
	if clave.lower() == 'salir': break
	persona[clave] = input(f"Ingrese el valor para '{clave}': ")
	print(f"\nDiccionario actual:\n{persona}\n")

print(f"\nDiccionario final:\n{persona}")