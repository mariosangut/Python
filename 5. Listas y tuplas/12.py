def multiplicar_matrices(matriz_a, matriz_b):
	"""Multiplica dos matrices y retorna el resultado"""
	filas_a = len(matriz_a)
	columnas_a = len(matriz_a[0])
	columnas_b = len(matriz_b[0])

	resultado = [[0 for _ in range(columnas_b)] for _ in range(filas_a)]

	for i in range(filas_a):
		for j in range(columnas_b):
			for k in range(columnas_a):
				resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

	return resultado

def mostrar_matriz(matriz, nombre="Matriz"):
    """Muestra una matriz en formato legible"""
    print(f"\n{nombre}:")
    for fila in matriz:
        print("[  " + "  ".join(f"[{valor}]" for valor in fila ) + "  ]")

matriz_a = [
	[1, 2, 3],
	[4, 5, 6]
]

matriz_b = [
	[7, 8],
	[9, 10],
	[11, 12]
]

matrices = [matriz_a, matriz_b]

mostrar_matriz(matrices[0], "Matriz A (2x3)")
mostrar_matriz(matrices[1], "Matriz B (3x2)")

producto = multiplicar_matrices(matrices[0], matrices[1])
mostrar_matriz(producto, "Producto A × B (2x2)")