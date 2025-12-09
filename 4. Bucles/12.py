frase = str(input("Escribe una frase : "))
letra = str(input("Escribe una letra : "))
i = 1
contador = 0

while i <= len(frase) :
    if frase[len(frase) - i] == letra :
        contador = contador +1
    i = i+1

print (f"La letra {letra} aparece {contador} veces")
