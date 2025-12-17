"""
===============================================================================
PROGRAMA: MAPAS (CHOROPLETH) COVID POR CCAA (ESPAÑA) - PRIMER TRIMESTRE 2021
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa genera 2 mapas (uno de Confirmados y otro de Recuperados) para
España, desglosados por Comunidad Autónoma (CCAA), y separados por mes
(Enero, Febrero, Marzo de 2021).

Salida del programa:
- grafico_ejercicio5_7_mapa_confirmados.png  (3 mapas: Ene/Feb/Mar)
- grafico_ejercicio5_7_mapa_recuperados.png  (3 mapas: Ene/Feb/Mar)

IDEA CLAVE:
-----------
Los CSV de COVID traen los nombres de regiones en inglés (Province_State) y el
GeoJSON usa otros nombres (acom_name). Por eso se hace un mapeo de nombres
para poder “unir” (merge) los datos del CSV con las geometrías del GeoJSON.

FUNCIONAMIENTO:
---------------
1) Lectura de CSV (enero, febrero, marzo) y GeoJSON de CCAA.
2) Filtrado para quedarnos solo con España y provincias válidas.
3) Conversión de nombres CSV -> nombres GeoJSON mediante un diccionario.
4) Totales por CCAA y mes (sumas de Confirmed y Recovered).
5) Preparación de datos en miles (para escalas más legibles).
6) Ajuste visual: mover Canarias hacia arriba (solo para representación).
7) Creación de 2 figuras:
   - Mapas de Confirmados (escala fija 0–400 miles, ticks cada 50)
   - Mapas de Recuperados (escala fija 0–50 miles, ticks cada 10)
8) Guardado de imágenes PNG en la carpeta del script.

===============================================================================
"""

import os
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from shapely.affinity import translate


# ---------------------------------------------------------------------------
# Mapeo de nombres del CSV (Province_State) -> nombres del GeoJSON (acom_name)
# ---------------------------------------------------------------------------
# Esto es imprescindible porque el merge se hace por "acom_name"
# y los nombres vienen distintos entre el CSV y el GeoJSON.

MAPA_CSV_A_GEO = {  "Andalusia": "Andalucía",
                    "Aragon": "Aragón",
                    "Asturias": "Principado de Asturias",
                    "Baleares": "Illes Balears",
                    "C. Valenciana": "Comunitat Valenciana",
                    "Canarias": "Canarias",
                    "Cantabria": "Cantabria",
                    "Castilla - La Mancha": "Castilla-La Mancha",
                    "Castilla y Leon": "Castilla y León",
                    "Catalonia": "Cataluña",
                    "Ceuta": "Ciudad Autónoma de Ceuta",
                    "Extremadura": "Extremadura",
                    "Galicia": "Galicia",
                    "La Rioja": "La Rioja",
                    "Madrid": "Comunidad de Madrid",
                    "Melilla": "Ciudad Autónoma de Melilla",
                    "Murcia": "Región de Murcia",
                    "Navarra": "Comunidad Foral de Navarra",
                    "Pais Vasco": "País Vasco",}

# Función auxiliar: resumen mensual por CCAA
def resumen_por_ccaa(df: pd.DataFrame, nombre_mes: str) -> pd.DataFrame:
    """
    Devuelve un DataFrame con los totales por CCAA para un mes.

    Pasos dentro:
    1) Filtrar solo España.
    2) Eliminar filas sin provincia o con provincia "Unknown".
    3) Convertir Province_State (CSV) -> acom_name (GeoJSON) con el diccionario.
    4) Agrupar por acom_name y sumar Confirmed y Recovered.
    5) Añadir columna "Mes" para poder concatenar varios meses.
    """
    df_spain = df[df["Country_Region"] == "Spain"].copy()
    df_spain = df_spain[df_spain["Province_State"].notna()]
    df_spain = df_spain[df_spain["Province_State"] != "Unknown"]

    # Crear una columna con el nombre exactamente como aparece en el GeoJSON
    df_spain["acom_name"] = df_spain["Province_State"].map(MAPA_CSV_A_GEO)

    resumen = (df_spain.groupby("acom_name")[["Confirmed", "Recovered"]].sum().reset_index())
    resumen["Mes"] = nombre_mes
    return resumen

# Rutas: carpeta del script + CSV/GeoJSON dentro de datos_covid
script_dir = os.path.dirname(os.path.abspath(__file__))

ruta_enero = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")
ruta_febrero = os.path.join(script_dir, "datos_covid", "COVID_01-02-2021.csv")
ruta_marzo = os.path.join(script_dir, "datos_covid", "COVID_01-03-2021.csv")

ruta_geojson = os.path.join(script_dir, "datos_covid", "georef_spain_comunidad_autonoma.geojson")

# Cargar CSV de cada mes
df_enero = pd.read_csv(ruta_enero)
df_febrero = pd.read_csv(ruta_febrero)
df_marzo = pd.read_csv(ruta_marzo)

# Crear resumen por CCAA y mes, y unirlo en un único DataFrame trimestral
res_enero = resumen_por_ccaa(df_enero, "Enero")
res_febrero = resumen_por_ccaa(df_febrero, "Febrero")
res_marzo = resumen_por_ccaa(df_marzo, "Marzo")

resumen_trimestre = pd.concat([res_enero, res_febrero, res_marzo], ignore_index=True)

# Pasar los valores a miles para que las escalas sean más manejables en los mapas
resumen_trimestre["Confirmados_miles"] = resumen_trimestre["Confirmed"] / 1_000
resumen_trimestre["Recuperados_miles"] = resumen_trimestre["Recovered"] / 1_000


# Cargar el mapa GeoJSON de CCAA y limpiar filas no deseadas
gdf_ccaa = gpd.read_file(ruta_geojson)

# El GeoJSON puede incluir una fila que no corresponde a una autonomía real
gdf_ccaa = gdf_ccaa[gdf_ccaa["acom_name"] != "Territorio no asociado a ninguna autonomía"].copy()

# Canarias queda muy abajo en el mapa real. Para mejorar legibilidad, movemos
# su geometría (NO modifica los datos, solo la representación).
mask_can = gdf_ccaa["acom_name"] == "Canarias"
gdf_ccaa.loc[mask_can, "geometry"] = gdf_ccaa.loc[mask_can, "geometry"].apply(
    lambda geom: translate(
        geom, xoff=4.5, 
        yoff=8.0))

# Configuración de meses a pintar (3 subplots: Enero, Febrero, Marzo)
meses = ["Enero", "Febrero", "Marzo"]

# Colormap y estilo general
cmap = plt.cm.Reds

# ===========================================================================
# MAPA 1: CONFIRMADOS
# ===========================================================================
# Escala fija para confirmados (en miles)
max_val_conf = 400
norm_conf = Normalize(vmin=0, vmax=max_val_conf)

fig1, axes1 = plt.subplots(1, 3, figsize=(15, 5))

for ax, mes in zip(axes1, meses):
    # Filtrar datos del mes actual
    datos_mes = resumen_trimestre[resumen_trimestre["Mes"] == mes]

    # Unir geometrías (gdf_ccaa) con datos del mes (Confirmados_miles)
    gdf_mes = gdf_ccaa.merge(datos_mes[["acom_name", "Confirmados_miles"]],on="acom_name",how="left",)

    # Dibujar el mapa
    gdf_mes.plot(
        column="Confirmados_miles",
        ax=ax,
        cmap=cmap,
        norm=norm_conf,
        edgecolor="black",
        linewidth=0.4,)

    ax.set_title(mes)
    ax.set_axis_off()

# Barra de color (leyenda continua)
sm1 = ScalarMappable(norm=norm_conf, cmap=cmap)
sm1.set_array([])

cbar1 = fig1.colorbar(
    sm1,
    ax=axes1.ravel().tolist(),
    fraction=0.035,
    pad=0.08,)  # separación con los mapas

cbar1.set_label("Casos confirmados (miles)")

# Ticks cada 50: 0, 50, 100, ..., 400
ticks_conf = np.arange(0, max_val_conf + 1, 50)
cbar1.set_ticks(ticks_conf)
cbar1.set_ticklabels([str(int(t)) for t in ticks_conf])

fig1.suptitle(
    "Casos confirmados de COVID por comunidad autónoma\n"
    "España, primer trimestre de 2021",
    y=0.94,)

# Ajuste para dejar espacio a la barra de color y al título
plt.tight_layout(rect=[0, 0, 0.86, 0.9])

salida_conf = os.path.join(script_dir, "grafico_ejercicio5_7_mapa_confirmados.png")
fig1.savefig(salida_conf, dpi=200)

# ===========================================================================
# MAPA 2: RECUPERADOS
# ===========================================================================
# Escala fija para recuperados (en miles)
max_val_rec = 50
norm_rec = Normalize(vmin=0, vmax=max_val_rec)

fig2, axes2 = plt.subplots(1, 3, figsize=(15, 5))

for ax, mes in zip(axes2, meses):
    datos_mes = resumen_trimestre[resumen_trimestre["Mes"] == mes]

    gdf_mes = gdf_ccaa.merge(
        datos_mes[["acom_name", "Recuperados_miles"]],
        on="acom_name",
        how="left",)

    gdf_mes.plot(
        column="Recuperados_miles",
        ax=ax,
        cmap=cmap,
        norm=norm_rec,
        edgecolor="black",
        linewidth=0.4,)

    ax.set_title(mes)
    ax.set_axis_off()

sm2 = ScalarMappable(norm=norm_rec, cmap=cmap)
sm2.set_array([])

cbar2 = fig2.colorbar(
    sm2,
    ax=axes2.ravel().tolist(),
    fraction=0.035,
    pad=0.08,)
cbar2.set_label("Casos recuperados (miles)")

# Ticks cada 10: 0, 10, 20, 30, 40, 50
ticks_rec = np.arange(0, max_val_rec + 1, 10)
cbar2.set_ticks(ticks_rec)
cbar2.set_ticklabels([str(int(t)) for t in ticks_rec])

fig2.suptitle(
    "Casos recuperados de COVID por comunidad autónoma\n"
    "España, primer trimestre de 2021",
    y=0.94,)

plt.tight_layout(rect=[0, 0, 0.86, 0.9])

salida_rec = os.path.join(script_dir, "grafico_ejercicio5_7_mapa_recuperados.png")
fig2.savefig(salida_rec, dpi=200)
