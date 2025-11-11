n = int(input("Introduce un número entero: "))

for i in range(1, n + 1):
    num = 2 * i - 1
    for j in range(num, 0, -2):
        print(j, end=" ")
    print() 
