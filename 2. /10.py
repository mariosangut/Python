"""Escribir un programa que pregunte por consola por los productos 
de una cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos 
en una línea distinta."""

cestaCompra = input("Introduce los productos de la cesta de la compra: ")
cestaCompra = cestaCompra.replace(",", "\n")
print(f"Los productos de la cesta de la compra son:\n{cestaCompra}")                                