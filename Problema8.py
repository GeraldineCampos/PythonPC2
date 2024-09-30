# Función para calcular el factorial de un número
def factorial(n):
    # Verificar si el número es negativo
    if n < 0:
        return "El factorial no está definido para números negativos."
    # Caso base: el factorial de 0 es 1
    elif n == 0:
        return 1
    # Calcular el factorial usando un bucle
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

# Ejemplo de uso
numero = int(input("Ingrese un número entero no negativo: "))
print(f"El factorial de {numero} es: {factorial(numero)}")