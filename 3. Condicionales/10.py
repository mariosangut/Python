tipoPizza = input("Que tipo de pisa desea (Vegetariana / normal): ").lower()

if tipoPizza == "vegetariana":
    print("Ingredientes vegetarianos disponibles:\n1) Pimiento\n2) Tofu")
    eleccion = input("Elige un ingrediente (pimiento/tofu): ").lower()
    if eleccion == "pimiento" or eleccion == "1":
        ingrediente = "pimiento"
    elif eleccion == "tofu" or eleccion == "2":
        ingrediente = "tofu"
    else:
        print("Opción no válida. Se seleccionará pimiento por defecto.")
    print(f"La pizza elegida es vegetariana y lleva: tomate, mozzarella y {ingrediente}")

elif tipoPizza == "normal":
    print ("Elige un ingrediente no vegetariano disponible:\n1) Peperoni\n2) Jamón\n3) Salmón")
    eleccion =  input("Elige un ingrediente (Peperoni/Jamón/Salmón): ").lower()
    if eleccion == "Peperoni" or eleccion == "1":
        ingrediente = "peperoni"
    elif eleccion == "Jamon" or eleccion == "2":
        ingrediente = "Jamon"
    elif eleccion == "Salmon" or eleccion == "3":
        ingrediente = "Salmon"
    else: 
        print("Opción no valida")
    print (f"La pizza elegida es no vegatariana y lleva: tomate, mozzarella y {ingrediente}")

else:
    print ("Opción de pizza no válida")
        
