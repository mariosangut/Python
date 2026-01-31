directorio_texto = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7".split('\n')
campos, directorio = directorio_texto[0].split(';'), {}

for linea in directorio_texto[1:]:
	valores = linea.split(';')
	nif, cliente = valores[0], {}
	for i in range(1, len(campos)):
		if campos[i] == 'descuento':
			cliente[campos[i]] = float(valores[i])
		else:
			cliente[campos[i]] = valores[i]
	
	directorio[nif] = cliente

print(directorio)