dic = {
	'nombre': '',
	'edad': 0,
	'direccion': '',
	'telefono': ''
}

dic['nombre'] = input("Ingrese su nombre: ")
dic['edad'] = int(input("Ingrese su edad: "))
dic['direccion'] = input("Ingrese su direccion: ")
dic['telefono'] = input("Ingrese su telefono: ")

print(f"{dic['nombre']} tiene {dic['edad']} años, vive en {dic['direccion']} y su número de teléfono es {dic['telefono']}")