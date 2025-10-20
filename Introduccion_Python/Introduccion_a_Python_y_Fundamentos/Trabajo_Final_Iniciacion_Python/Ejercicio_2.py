# ------------------------------
# Análisis de notas de una clase
# ------------------------------
# Datos: lista de diccionarios, uno por alumno con sus calificaciones.
# Funciones:
# 1) suspensos_asignaturas(): cuenta cuántos suspenden por asignatura.
# 2) media_notas(): calcula y muestra la media de cada alumno.
# 3) alumnos_aprobados(): lista los alumnos con media >= 5.
# Separar cálculos de la estructura de datos facilita cambios y pruebas.

clase_1 = [
    {"Alumno": "Alumno_1", "Latin": 8, "Castellano": 8, "Frances": 9, "Ingles": 4},
    {"Alumno": "Alumno_2", "Latin": 7, "Castellano": 6, "Frances": 7, "Ingles": 2},
    {"Alumno": "Alumno_3", "Latin": 10, "Castellano": 7, "Frances": 8, "Ingles": 9},
    {"Alumno": "Alumno_4", "Latin": 4, "Castellano": 4, "Frances": 3, "Ingles": 2},
    {"Alumno": "Alumno_5", "Latin": 9, "Castellano": 8, "Frances": 9, "Ingles": 6}
]


def suspensos_asignaturas(clase_1):
    """ Recorre la clase y cuenta cuántos alumnos suspenden cada asignatura.
    Muestra por pantalla el total de suspensos por materia. """
    
    asignaturas = ["Latin", "Castellano", "Frances", "Ingles"]
    umbral_suspenso = 5  # Nota estrictamente menor a 5 se considera suspenso
    # Contador por asignatura inicializado a 0
    contador = {s: 0 for s in asignaturas}

    # Para cada alumno, revisar todas las asignaturas y acumular suspensos
    for alumno in clase_1:
        for s in asignaturas:
            if alumno[s] < umbral_suspenso:
                contador[s] = contador[s] + 1

    # Salida legible: “X se ha suspendido por N alumnos”
    for s in asignaturas:
        print(s, "se ha suspendido por", contador[s], "alumnos")


def media_notas(clase_1):
    """ Calcula la media simple de cada alumno sobre las asignaturas listadas
    y la muestra por pantalla. """
    
    asignaturas = ["Latin", "Castellano", "Frances", "Ingles"]
    for alumno in clase_1:
        suma = 0
        contador = 0

        # Sumar notas de todas las asignaturas y contar cuántas hay
        for asignatura in asignaturas:
            suma = suma + alumno[asignatura]
            contador += 1

        # Media aritmética: suma total / número de asignaturas
        media = suma / contador
        print(alumno["Alumno"], "ha tenido una nota media de", media)


def alumnos_aprobados(clase_1):
    """ Determina qué alumnos aprueban el curso. Criterio:
    media de sus asignaturas >= umbral_aprobado. """
    
    asignaturas = ["Latin", "Castellano", "Frances", "Ingles"]
    umbral_aprobado = 5
    aprobados = []

    # Para cada alumno, calcular su media y decidir si aprueba
    for alumno in clase_1:
        suma = 0

        # Sumar las notas de todas las asignaturas del alumno
        for asignatura in asignaturas:
            suma = suma + alumno[asignatura]

        # Dividir por el número de asignaturas para obtener la media
        media = suma / len(asignaturas)

        # Si cumple el umbral, añadir su nombre a la lista de aprobados
        if media >= umbral_aprobado:
            aprobados.append(alumno["Alumno"])

    # Salida consolidada en una sola línea separada por comas
    print("Los alumnos que han aprobado el curso son:", ", ".join(aprobados))


# Bloque principal: ejecuta el flujo completo de informes
print("\n=== Suspensos por asignatura ===")
suspensos_asignaturas(clase_1)

print("\n=== Media de notas por alumno ===")
media_notas(clase_1)

print("\n=== Alumnos aprobados ===")
alumnos_aprobados(clase_1)