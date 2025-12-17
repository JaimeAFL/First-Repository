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


# Datos
nombres = np.array(["Francisco", "Lucía", "Juan", "Paula", "Alba"])
asignaturas = np.array(["HTML/CSS", "JavaScript", "Base de datos", "Programación"])

notas = np.array(
    [
        [9, 4, 8, 3],
        [7, 8, 10, 5],
        [10, 8, 6, 8],
        [7, 4, 8, 4],
        [8, 5, 6, 5],],dtype=int,)

# Funciones
def mostrar_suspensos(notas, asignaturas, umbral=5):
    suspensos_por_asig = (notas < umbral).sum(axis=0)

    for asig, n_suspensos in zip(asignaturas, suspensos_por_asig):
        print(f"{asig} se ha suspendido por {n_suspensos} alumnos")
    print()


def calcular_media(nombres, notas):
    medias = notas.mean(axis=1)

    for nombre, media in zip(nombres, medias):
        print(f"{nombre} ha obtenido una nota media de {media:.2f}")
    print()


def calcular_aprobados(nombres, notas, umbral=5):
    medias = notas.mean(axis=1)
    sin_suspensos = (notas >= umbral).all(axis=1)

    aprobados = nombres[(medias >= umbral) & sin_suspensos]

    if aprobados.size == 0:
        print("No hay alumnos que hayan aprobado el curso.")
    else:
        print("Los alumnos que han aprobado el curso son:", ", ".join(aprobados))
    print()


# Ejecución
mostrar_suspensos(notas, asignaturas)
calcular_media(nombres, notas)
calcular_aprobados(nombres, notas)