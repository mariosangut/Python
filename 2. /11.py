"""Escribir un programa que pregunte el nombre el un producto, su precio y 
un número de unidades y muestre por pantalla una cadena con el nombre 
del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""

# Solicitar datos al usuario
nombre = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))

# Calcular el coste total
coste_total = precio * unidades

# Mostrar la cadena formateada
print(f"Producto: {nombre} {precio:06.2f} {unidades:03d} {coste_total:08.2f}")
