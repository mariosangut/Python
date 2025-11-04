cliente = int(input("Introduce tu edad: "))

if cliente < 4:
    entrada = 0
elif cliente >=4 and cliente <=18:
    entrada = 5
elif cliente > 18:
    entrada = 10

print (f"Si usted quiere entrar deberá de pagar {entrada}€")