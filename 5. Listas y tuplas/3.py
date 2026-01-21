# Definir las listas
asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []

# Pedir los datos de las notas
for asignatura in asignaturas:
    nota = int(input(f"Que nota has sacado en {asignatura}: "))
    notas.append(nota)
    
print ("")
# Mostrar los resultados de las notas
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")