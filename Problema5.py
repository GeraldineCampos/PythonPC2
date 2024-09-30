# Función para verificar si un número es primo
def es_primo(Número):
    if Número < 2:
        return False
    for i in range(2, int(Número ** 0.5) + 1):
        if Número % i == 0:
            return False
    return True

# Sumar los números primos menores que 100
suma_primos = 0
for num in range(2, 100):
    if es_primo(num):
        suma_primos += num

print(f"La suma de todos los números primos menores que 100 es: {suma_primos}")