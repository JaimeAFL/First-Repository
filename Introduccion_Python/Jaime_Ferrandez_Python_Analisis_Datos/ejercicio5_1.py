"""
===============================================================================
CARGA Y ANÁLISIS BÁSICO DE UN CSV CON PANDAS
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Lee un archivo CSV con datos (en este caso, COVID) usando Pandas
y muestra un análisis básico por pantalla:
- Estructura del DataFrame (tipos de datos y valores no nulos)
- Cantidad de valores faltantes (NaN) por columna
- Las primeras 5 filas para ver una muestra del contenido

FUNCIONAMIENTO:
---------------
1) Lee el CSV desde una ruta definida.
2) Muestra .info() para revisar columnas, tipos y no nulos.
3) Calcula valores faltantes con isna().sum().
4) Muestra una vista previa con head().

===============================================================================
"""

import pandas as pd
import os


# Carpeta donde está este script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta completa al CSV dentro de la subcarpeta "datos_covid"
ruta_csv = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")

# Leer el CSV y cargarlo en un DataFrame de pandas
df = pd.read_csv(ruta_csv)

# Mostrar información general del DataFrame
print("Información del DataFrame (ENERO)")
print("---------------------------------")
df.info()
print()

# Contar los valores faltantes (NaN) por columna
#    df.isna() -> DataFrame de True/False
#    .sum()    -> cuenta los True (uno por cada valor faltante)

print("Datos faltantes por columna")
print("---------------------------")
print(df.isna().sum())
print()

# Mostrar una vista previa de los datos
#    df.head() devuelve las primeras 5 filas por defecto
print("Primeras 5 filas del DataFrame")
print("------------------------------")
print(df.head())