def decimal_a_binario(numero):
	if numero == 0:
		return "0"
	
	binario = ""
	while numero > 0:
		binario = str(numero % 2) + binario
		numero //= 2
	
	return binario


def binario_a_decimal(binario):
	decimal = 0
	for i, digito in enumerate(reversed(binario)):
		if digito in ['0', '1']:
			decimal += int(digito) * (2 ** i)
		else:
			raise ValueError("El binario contiene dígitos inválidos")
	
	return decimal


print(decimal_a_binario(10))     
print(binario_a_decimal("11001"))