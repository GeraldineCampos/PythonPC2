# Lista de meses para convertir de nombre a número
meses = [
         "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", 
         "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]

# Función para convertir la fecha al formato AAAA-MM-DD
def convertir_fecha(fecha):
    try:
        # Caso 1: Formato con números (MM/DD/AAAA)
        if '/' in fecha:
            mes, dia, año = fecha.split('/')
            mes, dia, año = int(mes), int(dia), int(año)
        # Caso 2: Formato con el mes en palabras (Mes Día, Año)
        else:
            partes = fecha.replace(",", "").split()
            mes = meses.index(partes[0]) + 1  # Convertir el nombre del mes a su número
            dia = int(partes[1])
            año = int(partes[2])
        
        # Devolver la fecha en formato AAAA-MM-DD, con mes y día de dos dígitos
        return f"{año:04d}-{mes:02d}-{dia:02d}"
    
    except Exception as e:
        return "Error: formato de fecha no válido."

# Solicitar al usuario una fecha en el formato descrito
fecha_usuario = input("Ingrese una fecha (ej. 9/8/1636 o Septiembre 8, 1636): ")

# Convertir la fecha y mostrar el resultado
resultado = convertir_fecha(fecha_usuario)
print("Fecha convertida:", resultado)