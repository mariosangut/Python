# Definir listas
loteria = []

for i in range(1,7):
    numero = int(input("Introduce los numeros ganadores de la loteria: "))
    loteria.append(numero)


loteria.sort()
print (f"Los numeros ganadores de la loteria son: {loteria}")

# Ordenamos los datos sin tocar la lista original
ordenados = sorted(loteria,reverse=True,)