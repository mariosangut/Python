pesoPayasos = 112
pesoMuñecas = 75

payasosVendidos = float(input("¿Cuántos payasos se han vendido? "))
muñecasVendidas = float(input("¿Cuántas muñecas se han vendido? "))

pesoPedido = (payasosVendidos * pesoPayasos) + (muñecasVendidas * pesoMuñecas)

print (f"El peso del ultimo pedido de payasos y muñecas fue de: {pesoPedido} g")