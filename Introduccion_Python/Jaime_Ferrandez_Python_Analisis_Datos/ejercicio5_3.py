"""
===============================================================================
PROVINCIAS SIN CASOS DE RECUPERADOS (FILTRADO CON PANDAS)
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa carga un CSV de COVID y detecta provincias/estados que no tienen
casos de pacientes recuperados (Recovered = 0 o vacío). Después elimina filas
sin provincia/estado (Province_State vacío) y muestra una tabla final con las
parejas únicas (Province_State, Country_Region).

IDEA CLAVE:
-----------
En este dataset puede haber valores faltantes (NaN) en "Recovered". Para poder
comparar correctamente, se sustituyen los NaN por 0, y luego se filtra:
    Recovered == 0

FUNCIONAMIENTO:
---------------
1) Lectura del CSV:
   - Se carga el archivo en un DataFrame con pandas.read_csv().

2) Filtrado por recuperados:
   - dataframe["Recovered"].fillna(0) reemplaza NaN por 0.
   - Se seleccionan solo las filas donde Recovered == 0.

3) Filtrado por provincia válida:
   - Se descartan filas donde "Province_State" está vacío (NaN),
     porque queremos provincias/estados reales.

4) Selección y limpieza de columnas:
   - Se extraen solo las columnas ["Province_State", "Country_Region"].
   - drop_duplicates() elimina combinaciones repetidas.
   - reset_index(drop=True) reordena el índice desde 0.

5) Salida:
   - Se imprime el resultado final.

===============================================================================
"""

import os
import pandas as pd


# Carpeta donde está este script (por ejemplo, ejercicio5_3.py)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta completa al CSV dentro de la subcarpeta "datos_covid"
ruta_csv = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")

# Leer el CSV y cargarlo en un DataFrame de pandas
df = pd.read_csv(ruta_csv)

# Filtrar filas donde no hay pacientes recuperados
#   - df["Recovered"] puede tener valores numéricos o NaN.
#   - fillna(0) convierte NaN en 0 para tratarlos como "sin recuperados".
#   - Comparamos con 0 para quedarnos con las filas sin recuperados.
sin_recuperados = df[df["Recovered"].fillna(0) == 0]

# Eliminar filas sin provincia/estado
#   - Algunas filas pueden tener Province_State = NaN (desconocido).
#   - Solo queremos las que tienen una provincia o estado definido.
sin_recuperados = sin_recuperados[sin_recuperados["Province_State"].notna()]

# Extraer solo las columnas relevantes y quitar duplicados
#   - Nos quedamos con "Province_State" y "Country_Region".
#   - drop_duplicates() evita repetir la misma provincia-país varias veces.
#   - reset_index(drop=True) reorganiza el índice desde 0.
provincias_paises = (sin_recuperados[["Province_State", "Country_Region"]].drop_duplicates().reset_index(drop=True))

# Mostrar el resultado por pantalla
print("Provincias sin casos de pacientes recuperados (enero 2021)")
print("----------------------------------------------------------")
print(provincias_paises)