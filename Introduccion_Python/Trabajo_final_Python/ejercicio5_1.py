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

# Ruta del archivo CSV (ajusta si cambia tu estructura de carpetas)
ruta_csv = ("/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/" "datos_covid/COVID_01-01-2021.csv")

# Leer el CSV y cargarlo en un DataFrame
df = pd.read_csv(ruta_csv)

# Mostrar información general del DataFrame (columnas, tipos, nulos, memoria)
print("Información del DataFrame (ENERO)")
print("---------------------------------")
# df.info() imprime directamente; por eso NO se envuelve en print()
df.info()
print()

# Contar valores faltantes por columna
print("Datos faltantes por columna")
print("---------------------------")
print(df.isna().sum())
print()

# Mostrar las primeras 5 filas como vista previa
print("Primeras 5 filas del DataFrame")
print("------------------------------")
print(df.head())