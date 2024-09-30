Alumnos = []

# Cantidad de alumnos a ingresar
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Ingresar los datos de cada alumno
for i in range(cantidad_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ").strip()
    notas = []

    # Ingrese 3 calificaciones para el alumno
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la calificación {j + 1} para {nombre}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico para la calificación.")
    
    # Agregar el alumno y sus calificaciones a la lista de alumnos
    Alumnos.append({
        'Alumno': nombre,
        'Notas': notas
    })

# Mostrar el listado completo de los alumnos
print("\nListado completo de alumnos:")
for Alumno in Alumnos:
    print(f"Alumno: {Alumno['Alumno']}, Notas: {Alumno['Notas']}")