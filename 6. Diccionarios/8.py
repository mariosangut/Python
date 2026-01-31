# Crear diccionario de traducción
print("Introduce los pares palabra:traducción separados por comas")
print("Ejemplo: gato:cat,perro:dog,casa:house")
entrada = input("> ")

diccionario = {}
pares = entrada.split(",")
for par in pares:
	if ":" in par:
		es, en = par.strip().split(":")
		diccionario[es.strip()] = en.strip()

print("\nIntroduce una frase en español:")
frase = input("> ")

palabras = frase.split()
traduccion = []

for palabra in palabras:
	palabra_limpia = palabra.lower().strip(".,!?;:")
	puntuacion = palabra[len(palabra_limpia):]
	
	if palabra_limpia in diccionario:traduccion.append(diccionario[palabra_limpia] + puntuacion)
	else:traduccion.append(palabra)

print("\nTraducción: " + " ".join(traduccion))