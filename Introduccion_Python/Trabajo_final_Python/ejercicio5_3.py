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

import pandas as pd

# Ruta del archivo CSV (ajusta si cambia tu estructura de carpetas)
ruta_csv = ("/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/" "datos_covid/COVID_01-01-2021.csv")

# Leer el CSV y cargarlo en un DataFrame
df = pd.read_csv(ruta_csv)

# Filtrar filas donde "Recovered" es 0 o NaN (NaN se trata como 0)
sin_recuperados = df[df["Recovered"].fillna(0) == 0]

# Quedarnos solo con filas donde sí existe provincia/estado
sin_recuperados = sin_recuperados[sin_recuperados["Province_State"].notna()]

# Extraer solo las columnas relevantes y eliminar duplicados
provincias_paises = (sin_recuperados[["Province_State", "Country_Region"]].drop_duplicates().reset_index(drop=True))

# 5) Mostrar el resultado
print("=== Provincias sin casos de pacientes recuperados (enero 2021) ===")
print(provincias_paises)