print ("Programa que hace la serie de fibonacci")
print ("Hecho por Arguello Viveros Jesus Antonio y Corona Aguilera Joshua Amaitzin")
n = int(input("Introduce el número de términos: "))

# Inicialización de los primeros términos
a, b = 0, 1
fibonacci = []
contador = 0

# Generar la serie con while
while contador < n:
    fibonacci.append(a)
    a, b = b, a + b  # Actualizar los valores
    contador += 1

print("Serie de Fibonacci:", fibonacci)
