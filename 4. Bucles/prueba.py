contraseña = "me gustas tu"

while True:
    respuesta = input("Introduce la contraseña: ")
    if respuesta == contraseña:
        print ("Contraseña correcta")
        break
    else:
        print ("Continua intentandolo")
