# --------------------------------------------------------------
# Análisis de calificaciones con NumPy 
# --------------------------------------------------------------
# Estructura:

# 1) Datos: tres estructuras NumPy
#    - nombres: vector 1D con los nombres de alumnos
#    - asignaturas: vector 1D con los nombres de asignaturas
#    - notas: matriz 2D (filas=alumnos, columnas=asignaturas) con enteros
# 2) mostrar_suspensos(notas, asignaturas, umbral=5):

#    - calcula cuántos alumnos suspenden cada asignatura (nota < umbral)
#    - imprime un mensaje por asignatura

# 3) calcular_media(nombres, notas):
#    - calcula la media por alumno (media por fila)
#    - imprime “<nombre> ha obtenido una nota media de <media>”

# 4) calcular_aprobados(nombres, notas, umbral=5):
#    - condición 1: media del alumno >= umbral
#    - condición 2: no suspender ninguna asignatura (todas sus notas >= umbral)
#    - imprime la lista de alumnos que aprueban el curso

import numpy as np

# Crea un array 1D con los nombres de los alumnos y con los nombres 
# de las asignaturas en el orden de las columnas de 'notas'
nombres = np.array(["Francisco","Lucía","Juan","Paula","Alba"])
asignaturas = np.array(["HTML/CSS","JavaScript","Base de datos","Programación"])

# Array 2D (matriz) con las notas.
# Filas -> alumnos en el mismo orden que 'nombres'.
# Columnas -> asignaturas en el mismo orden que 'asignaturas'.
notas = np.array([
                [9, 4, 8, 3],
                [7, 8, 10, 5],
                [10,8, 6, 8],
                [7, 4, 8, 4],
                [8, 5, 6, 5]],dtype=int)

def mostrar_suspensos(notas, asignaturas, umbral=5):
    """
    Recibe:
      - notas: array 2D (alumnos x asignaturas)
      - asignaturas: array 1D con nombres de asignaturas
      - umbral: nota mínima para aprobar (por defecto 5)
    Efecto:
      - Imprime para cada asignatura cuántos alumnos han sacado una nota < umbral.
    """
    # Crea una máscara booleana True/False donde True indica suspenso (nota < umbral).
    # Agrega por columnas (axis=0) para contar suspensos en cada asignatura.
    susp = np.sum(notas < umbral, axis=0)

    # Recorre las columnas con su índice y muestra el total de suspensos por asignatura.
    for i in range(notas.shape[1]):
        print(f"{asignaturas[i]} se ha suspendido por {susp[i]} alumnos")
    
    # Salto de línea para separar lo que sale por la terminal.
    print()

def calcular_media(nombres, notas):
    """
    Recibe:
      - nombres: array 1D con nombres de alumnos
      - notas: array 2D (alumnos x asignaturas)
    Efecto:
      - Imprime la nota media de cada alumno.
    """
        # Calcula la media por fila (axis=1) que corresponde a cada alumno.
    medias = np.mean(notas, axis=1)

    # Recorre las filas (alumnos) y muestra su media con 2 decimales.
    for i in range(notas.shape[0]):
        print(f"{nombres[i]} ha obtenido una nota media de {medias[i]:.2f}")
    print()

def calcular_aprobados(nombres, notas, umbral=5):
    """
    Condiciones de aprobado:
      1) Media del alumno ≥ umbral.
      2) No suspender ninguna asignatura (todas las notas de su fila ≥ umbral).
    Efecto:
      - Imprime la lista de alumnos que cumplen ambas condiciones.
    """
    medias = np.mean(notas, axis=1)

    # Verifica, por cada alumno, si no tiene ningún suspenso.
    # (notas >= umbral) crea una máscara booleana 2D.
    # .all(axis=1) comprueba que TODAS las columnas de cada fila cumplan la condición.
    sin_suspensos = np.all(notas >= umbral, axis=1)
    aprobados = nombres[(medias >= umbral) & (sin_suspensos)]
    print("Los alumnos que han aprobado el curso son:", ", ".join(aprobados))
    print()

# Llamadas a las funciones para mostrar los resultados.
mostrar_suspensos(notas, asignaturas)
calcular_media(nombres, notas)
calcular_aprobados(nombres, notas)