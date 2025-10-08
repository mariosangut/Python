"""Escribir un programa que pregunte al usuario la fecha de 
su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
el día, el mes y el año. Adaptar el programa anterior para que 
también funcione cuando el día o el mes se introduzcan con un solo carácter."""

fecha = input("Introduce la fecha en formato 'dd/mm/aaaa' ")
print(f"Día: {fecha.split('/')[0]} Mes: {fecha.split('/')[1]} Año: {fecha.split('/')[2]}")