Números = []

while True:
    # Preguntar si se desea ingresar un número
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().lower()
    
    if respuesta == 'si':
        # Solicitar que se ingrese el número
        try:
            Número = int(input("Ingrese el número: "))
            Números.append(Número)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif respuesta == 'no':
        # Salir del bucle si se decide no continuar
        break
    else:
        # En caso de que la respuesta no sea válida
        print("Por favor, responda con 'SI' o 'NO'.")

# Calcular la cantidad de números pares e impares
Cantidad_Pares = sum(1 for num in Números if num % 2 == 0)
Cantidad_Impares = len(Números) - Cantidad_Pares

# Mostrar los resultados
print(f"Números ingresados: {Números}")
print(f"Cantidad de números pares: {Cantidad_Pares}")
print(f"Cantidad de números impares: {Cantidad_Impares}")