altura = float(input("Cuanto mides? "))
peso = float(input("Cuanto pesas? "))
indice = peso / (altura * altura)  # altura ** 2 --> ^2
print(f"Su indice de masa es : {round(indice,(2))}")
