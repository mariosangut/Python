p = input("Introduce una palabra: ");
print(f"La palabra {p} es un palíndromo.") if p == p[::-1] else print(f"La palabra {p} no es un palíndromo.")