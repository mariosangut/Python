nombre = input("Introduce tu nombre: ").strip()
sexo = input("Introduce tu sexo (Masculino / Femenino): ").strip().lower()

primera = nombre[0].upper()
grupo = 'B'

if sexo.startswith('f') and primera < 'M':
    grupo = 'A'
elif sexo.startswith('m') and primera > 'N':
    grupo = 'A'

print(f"Pertenece al grupo {grupo}")
