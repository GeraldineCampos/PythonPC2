# Función para encontrar los divisores propios de un número
def divisores_propios(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

# Función para verificar si un número es perfecto
def es_perfecto(n):
    return sum(divisores_propios(n)) == n

# Mostrar todos los números perfectos menores que 1000
print("Los números perfectos menores que 1000 son:")
for num in range(1, 1000):
    if es_perfecto(num):
        print(num)