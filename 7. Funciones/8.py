def calcular_estadisticas(numeros):
	n = len(numeros)
	
	if n == 0:
		return None
	
	media = sum(numeros) / n
	varianza = sum((x - media) ** 2 for x in numeros) / (n - 1) if n > 1 else 0
	desviacion_tipica = varianza ** 0.5
	
	return {
		'media': media,
		'varianza': varianza,
		'desviacion_tipica': desviacion_tipica
	}

if __name__ == "__main__":
	muestra = [2, 4, 6, 8, 10]
	resultado = calcular_estadisticas(muestra)
	print(resultado)