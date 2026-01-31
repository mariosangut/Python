import math

def area_circulo(radio):
	return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
	return area_circulo(radio) * altura

radio = 5
altura = 10

print(f"Área del círculo (radio {radio}): {area_circulo(radio):.2f}")
print(f"Volumen del cilindro (radio {radio}, altura {altura}): {volumen_cilindro(radio, altura):.2f}")