def mcd(a, b):
	while b != 0:
		a, b = b, a % b
	return abs(a)


def mcm(a, b):
	return abs(a * b) // mcd(a, b)

num1 = 48
num2 = 18

print(f"MCD de {num1} y {num2}: {mcd(num1, num2)}")
print(f"MCM de {num1} y {num2}: {mcm(num1, num2)}")