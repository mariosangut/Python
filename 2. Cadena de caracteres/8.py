""" Escribir un programa que pregunte por consola el precio 
de un producto en euros con dos decimales y muestre por 
pantalla el número de euros y el número de céntimos del
precio introducido."""

precio = input("Intdouce el precio en euros con dos decimales: ")

print (f"Son {precio.split('.')[0]} euros y {precio.split('.')[1]} centimos")