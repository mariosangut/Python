def agregar_cliente(clientes):
	nif = input("NIF: ")
	if nif in clientes:
		print("El cliente ya existe."); return
	
	nombre, direccion, telefono, correo, preferente = input("Nombre: "), input("Dirección: "), input("Teléfono: "), input("Correo: "), input("¿Es preferente? (s/n): ").lower() == 's'
	
	clientes[nif] = {
		'nombre': nombre,
		'direccion': direccion,
		'telefono': telefono,
		'correo': correo,
		'preferente': preferente
	}

	print("Cliente añadido correctamente.\n")

def eliminar_cliente(clientes):
	nif = input("NIF del cliente a eliminar: ")
	if nif in clientes:
		del clientes[nif]
		print("Cliente eliminado correctamente.\n")
	else:
		print("Cliente no encontrado.\n")

def mostrar_cliente(clientes):
	nif = input("NIF del cliente: ")
	if nif in clientes:
		cliente = clientes[nif]
		print(f"\nNIF: {nif}")
		print(f"Nombre: {cliente['nombre']}")
		print(f"Dirección: {cliente['direccion']}")
		print(f"Teléfono: {cliente['telefono']}")
		print(f"Correo: {cliente['correo']}")
		print(f"Preferente: {'Sí' if cliente['preferente'] else 'No'}\n")
	else:
		print("Cliente no encontrado.\n")

def listar_todos(clientes):
	if not clientes:
		print("No hay clientes registrados.\n")
		return
	print("\n--- Lista de todos los clientes ---")
	for nif, cliente in clientes.items():
		print(f"{nif}: {cliente['nombre']}")
	print()

def listar_preferentes(clientes):
	preferentes = {nif: cliente for nif, cliente in clientes.items() if cliente['preferente']}
	if not preferentes:
		print("No hay clientes preferentes.\n")
		return
	print("\n--- Clientes preferentes ---")
	for nif, cliente in preferentes.items():
		print(f"{nif}: {cliente['nombre']}")
	print()

def main():
	clientes = {}
	
	while True:
		print("--- Gestión de clientes ---")
		print("1. Añadir cliente")
		print("2. Eliminar cliente")
		print("3. Mostrar cliente")
		print("4. Listar todos los clientes")
		print("5. Listar clientes preferentes")
		print("6. Terminar")
		
		opcion = input("Seleccione una opción: ")
		
		if opcion == '1':
			agregar_cliente(clientes)
		elif opcion == '2':
			eliminar_cliente(clientes)
		elif opcion == '3':
			mostrar_cliente(clientes)
		elif opcion == '4':
			listar_todos(clientes)
		elif opcion == '5':
			listar_preferentes(clientes)
		elif opcion == '6':
			print("¡Hasta luego!"); break
		else:
			print("Opción no válida.\n")

if __name__ == "__main__":
	main()