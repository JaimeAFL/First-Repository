"""
===============================================================================
PROGRAMA: ANÁLISIS DE CALIFICACIONES CON NUMPY
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa analiza las notas de varios alumnos en varias asignaturas usando
arrays de NumPy.

Estructura de datos:
- nombres: vector 1D con nombres de alumnos
- asignaturas: vector 1D con nombres de asignaturas (mismo orden que columnas)
- notas: matriz 2D (filas=alumnos, columnas=asignaturas) con enteros

FUNCIONAMIENTO:
---------------
1) mostrar_suspensos(notas, asignaturas, umbral=5):
   - Cuenta cuántos alumnos suspenden cada asignatura (nota < umbral)
   - Imprime el resultado por asignatura

2) calcular_media(nombres, notas):
   - Calcula la media por alumno (media de cada fila)
   - Imprime “<nombre> ha obtenido una nota media de <media>”

3) calcular_aprobados(nombres, notas, umbral=5):
   - Aprobado si:
       a) media >= umbral
       b) no suspende ninguna asignatura (todas sus notas >= umbral)
   - Imprime la lista de alumnos que aprueban el curso

===============================================================================
"""

import numpy as np


# Vector con los nombres del alumnado
nombres = np.array(["Francisco", "Lucía", "Juan", "Paula", "Alba"])

# Vector con los nombres de las asignaturas (en el mismo orden que las columnas de 'notas')
asignaturas = np.array(["HTML/CSS", "JavaScript", "Base de datos", "Programación"])

# Matriz de notas:
#   - Cada fila corresponde a un alumno (en el mismo orden que 'nombres')
#   - Cada columna corresponde a una asignatura (en el mismo orden que 'asignaturas')
notas = np.array(
    [
        [9, 4, 8, 3],
        [7, 8, 10, 5],
        [10, 8, 6, 8],
        [7, 4, 8, 4],
        [8, 5, 6, 5],],dtype=int,)

# Funciones
def mostrar_suspensos(notas, asignaturas, umbral=5):
    # (notas < umbral) devuelve una matriz de True/False con los suspensos
    # sum(axis=0) suma por columnas → número de suspensos en cada asignatura
    suspensos_por_asig = (notas < umbral).sum(axis=0)

    # Recorremos asignaturas y número de suspensos en paralelo
    for asig, n_suspensos in zip(asignaturas, suspensos_por_asig):
        print(f"{asig} se ha suspendido por {n_suspensos} alumnos")
    print()  # Línea en blanco para separar bloques de salida

def calcular_media(nombres, notas):
    # mean(axis=1) calcula la media por fila → media de cada alumno
    medias = notas.mean(axis=1)

    # Recorremos nombres y medias en paralelo
    for nombre, media in zip(nombres, medias):
        print(f"{nombre} ha obtenido una nota media de {media:.2f}")
    print()

def calcular_aprobados(nombres, notas, umbral=5):
    # Media por alumno (por filas)
    medias = notas.mean(axis=1)

    # (notas >= umbral) devuelve True/False por asignatura.
    # all(axis=1) comprueba todas las asignaturas de cada alumno
    # están aprobadas → True si no tiene ningún suspenso.
    sin_suspensos = (notas >= umbral).all(axis=1)

    # Condición compuesta:
    #   - media >= umbral
    #   - y además no tiene suspensos
    aprobados = nombres[(medias >= umbral) & sin_suspensos]

    if aprobados.size == 0:
        print("No hay alumnos que hayan aprobado el curso.")
    else:
        print("Los alumnos que han aprobado el curso son:", ", ".join(aprobados))
    print()

# Ejecución del programa
mostrar_suspensos(notas, asignaturas)
calcular_media(nombres, notas)
calcular_aprobados(nombres, notas)