asignaturas, notas = ["Matemáticas", "Física", "Química", "Biología", "Historia"], []
for a in asignaturas:
	n = input(f'¿Que has sacado en {a}? '); notas.append(float(n))
print()

suspensas = [a for a, n in zip(asignaturas, notas) if n < 5.0]

print("Debes repetir: ", end="")
for i in suspensas: print(i, end=" ")