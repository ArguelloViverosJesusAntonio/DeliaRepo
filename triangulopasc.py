print ("Programa que hace la funcion de el triangulo de pascal")
print ("Hecho por Arguello Viveros Jesus Antonio y Corona Aguilera Joshua Amaitzin")
filas = int(input("¿Cuántas filas del Triángulo de Pascal deseas generar? "))

if filas <= 0:
    print("Debes ingresar un número mayor que 0.")
else:
    triangulo = [[0] * filas for _ in range(filas)]

    i = 0
    while i < filas:
        triangulo[i][0] = 1  
        j = 1

        while j < i:
            triangulo[i][j] = triangulo[i-1][j-1] + triangulo[i-1][j]
            j += 1

        if i > 0:
            triangulo[i][i] = 1  

        i += 1

    i = 0
    while i < filas:
        print(" " * (filas - i), end="")
        j = 0

        while j <= i:
            print(triangulo[i][j], end=" ")
            j += 1

        print() 
        i += 1
