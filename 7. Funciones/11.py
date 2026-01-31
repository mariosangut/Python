def contar_palabras(cadena):
	palabras, frecuencia = cadena.lower().split(), {}
	
	for palabra in palabras:
		palabra = palabra.strip('.,!?;:')
		if palabra:
			frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
	
	return frecuencia


def palabra_mas_frecuente(diccionario):
	if not diccionario:
		return None
	
	palabra = max(diccionario, key=diccionario.get)
	return (palabra, diccionario[palabra])


texto = "Python es genial. Python es poderoso. Python es fácil de aprender"
print("Frecuencia de palabras:", contar_palabras(texto))
print("Palabra más repetida:", palabra_mas_frecuente(contar_palabras(texto)))