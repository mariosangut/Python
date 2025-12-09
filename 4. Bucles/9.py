contraseña = "pepe"
pregunta = input("Escribe tu contraseña : ")

if pregunta == contraseña :
        print ("Contraseña correcta")

else :     
    while pregunta != contraseña :
        print ("contraseña incorrecta, vuelve a introducirla")
        pregunta = input("Escribe tu contraseña : ")