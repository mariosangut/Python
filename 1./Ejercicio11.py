saldoInicial = float(input("Introduce el saldo inical: "))
saldoPrimerAño = saldoInicial + saldoInicial * 0.04
saldoSegundoAño = saldoPrimerAño + saldoPrimerAño * 0.04
saldoTercerAño = saldoSegundoAño + saldoSegundoAño * 0.04

print (f"Los ahorros del primer años son: {round(saldoPrimerAño,(2))} €")
print (f"Los ahorros del segundo años son: {round(saldoSegundoAño,(2))} €")
print (f"Los ahorros del tercer años son: {round(saldoTercerAño,(2))} €")