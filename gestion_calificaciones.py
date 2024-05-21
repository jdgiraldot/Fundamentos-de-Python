# Función para calcular el promedio de las calificaciones
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Función para encontrar la calificación más alta
def calificacion_mas_alta(calificaciones):
    return max(calificaciones)

# Función para encontrar la calificación más baja
def calificacion_mas_baja(calificaciones):
    return min(calificaciones)

# Función para categorizar las calificaciones
def categorizar_calificacion(calificacion):
    if 90 <= calificacion <= 100:
        return 'A'
    elif 80 <= calificacion <= 89:
        return 'B'
    elif 70 <= calificacion <= 79:
        return 'C'
    elif 60 <= calificacion <= 69:
        return 'D'
    else:
        return 'F'

# Listas para almacenar los nombres y calificaciones de los estudiantes
nombres_estudiantes = []
calificaciones_estudiantes = []

# Entrada de datos
while True:
    nombre = input("Ingrese el nombre del estudiante (o escriba 'salir' para finalizar): ")
    if nombre.lower() == 'salir':
        break
    calificacion = float(input("Ingrese la calificación de {}: ".format(nombre)))
    nombres_estudiantes.append(nombre)
    calificaciones_estudiantes.append(calificacion)

# Verificar que se ingresaron datos
if len(nombres_estudiantes) == 0:
    print("No se ingresaron datos de estudiantes.")
else:
    # Calcular promedio, calificación más alta y más baja
    promedio = calcular_promedio(calificaciones_estudiantes)
    calif_max = calificacion_mas_alta(calificaciones_estudiantes)
    calif_min = calificacion_mas_baja(calificaciones_estudiantes)

    # Categorizar las calificaciones
    categorias = [categorizar_calificacion(calificacion) for calificacion in calificaciones_estudiantes]

    # Mostrar resultados
    print("\nResultados:")
    print("Promedio de las calificaciones: {:.2f}".format(promedio))
    print("Calificación más alta: {:.2f}".format(calif_max))
    print("Calificación más baja: {:.2f}".format(calif_min))
    print("\nCategorías de calificaciones:")
    for i in range(len(nombres_estudiantes)):
        print("{}: {:.2f} - {}".format(nombres_estudiantes[i], calificaciones_estudiantes[i], categorias[i]))