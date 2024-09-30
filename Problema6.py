a, b = 0, 1

# Imprimir los términos de la serie de Fibonacci menores o iguales a 50
print("Serie de Fibonacci entre 0 y 50:")
while a <= 50:
    print(a, end=", ")
    a, b = b, a + b