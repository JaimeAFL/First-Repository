
import os
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from shapely.affinity import translate


# Mapeo de nombres del CSV (Province_State) -> nombres del GeoJSON (acom_name)
MAPA_CSV_A_GEO = {
    "Andalusia": "Andalucía",
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
    "Pais Vasco": "País Vasco",
    }


def resumen_por_ccaa(df: pd.DataFrame, nombre_mes: str) -> pd.DataFrame:
    """Totales confirmados y recuperados por comunidad autónoma para un mes."""
    df_spain = df[df["Country_Region"] == "Spain"].copy()
    df_spain = df_spain[df_spain["Province_State"].notna()]
    df_spain = df_spain[df_spain["Province_State"] != "Unknown"]

    df_spain["acom_name"] = df_spain["Province_State"].map(MAPA_CSV_A_GEO)

    resumen = (
        df_spain
        .groupby("acom_name")[["Confirmed", "Recovered"]]
        .sum()
        .reset_index()
    )
    resumen["Mes"] = nombre_mes
    return resumen


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Rutas CSV y GeoJSON
    ruta_enero = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")
    ruta_febrero = os.path.join(script_dir, "datos_covid", "COVID_01-02-2021.csv")
    ruta_marzo = os.path.join(script_dir, "datos_covid", "COVID_01-03-2021.csv")
    ruta_geojson = os.path.join(
        script_dir, "datos_covid", "georef_spain_comunidad_autonoma.geojson"
    )

    # DataFrames de cada mes
    df_enero = pd.read_csv(ruta_enero)
    df_febrero = pd.read_csv(ruta_febrero)
    df_marzo = pd.read_csv(ruta_marzo)

    res_enero = resumen_por_ccaa(df_enero, "Enero")
    res_febrero = resumen_por_ccaa(df_febrero, "Febrero")
    res_marzo = resumen_por_ccaa(df_marzo, "Marzo")

    resumen_trimestre = pd.concat(
        [res_enero, res_febrero, res_marzo],
        ignore_index=True
    )

    # Pasar a miles de casos
    resumen_trimestre["Confirmados_miles"] = resumen_trimestre["Confirmed"] / 1_000
    resumen_trimestre["Recuperados_miles"] = resumen_trimestre["Recovered"] / 1_000

    # Cargar mapa CCAA
    gdf_ccaa = gpd.read_file(ruta_geojson)
    gdf_ccaa = gdf_ccaa[
        gdf_ccaa["acom_name"] != "Territorio no asociado a ninguna autonomía"
    ].copy()

    # Mover Canarias para que no quede tan abajo (solo en la representación)
    mask_can = gdf_ccaa["acom_name"] == "Canarias"
    gdf_ccaa.loc[mask_can, "geometry"] = gdf_ccaa.loc[mask_can, "geometry"].apply(
        lambda geom: translate(geom, xoff=4.5, yoff=8.0)
    )

    # Máximo real de los datos (por si quieres verlo, aunque no lo usamos)
    max_conf_datos = resumen_trimestre["Confirmados_miles"].max()
    max_rec_datos = resumen_trimestre["Recuperados_miles"].max()

    # Fijamos la escala de la barra en 400 para ambos mapas (miles)
    max_val = 400

    cmap = plt.cm.Reds
    norm = Normalize(vmin=0, vmax=max_val)

    meses = ["Enero", "Febrero", "Marzo"]

    # -------------------- MAPA DE CONFIRMADOS --------------------
    fig1, axes1 = plt.subplots(1, 3, figsize=(15, 5))

    for ax, mes in zip(axes1, meses):
        datos_mes = resumen_trimestre[resumen_trimestre["Mes"] == mes]

        gdf_mes = gdf_ccaa.merge(
            datos_mes[["acom_name", "Confirmados_miles"]],
            on="acom_name",
            how="left"
        )

        gdf_mes.plot(
            column="Confirmados_miles",
            ax=ax,
            cmap=cmap,
            norm=norm,
            edgecolor="black",
            linewidth=0.4
        )

        ax.set_title(mes)
        ax.set_axis_off()

    sm1 = ScalarMappable(norm=norm, cmap=cmap)
    sm1.set_array([])

    cbar1 = fig1.colorbar(
        sm1,
        ax=axes1.ravel().tolist(),
        fraction=0.035,
        pad=0.08  # separación con el mapa
    )
    cbar1.set_label("Casos confirmados (miles)")

    # Ticks cada 50: 0, 50, 100, ..., 400
    ticks = np.arange(0, max_val + 1, 50)
    cbar1.set_ticks(ticks)
    cbar1.set_ticklabels([str(int(t)) for t in ticks])

    fig1.suptitle(
        "Casos confirmados de COVID por comunidad autónoma\n"
        "España, primer trimestre de 2021",
        y=0.94
    )

    plt.tight_layout(rect=[0, 0, 0.86, 0.9])

    salida_conf = os.path.join(script_dir, "grafico_ejercicio5_7_mapa_confirmados.png")
    fig1.savefig(salida_conf, dpi=200)

    # -------------------- MAPA DE RECUPERADOS --------------------
    # Escala específica para recuperados: 0–50 (miles)
    max_val_rec = 50
    norm_rec = Normalize(vmin=0, vmax=max_val_rec)

    fig2, axes2 = plt.subplots(1, 3, figsize=(15, 5))

    for ax, mes in zip(axes2, meses):
        datos_mes = resumen_trimestre[resumen_trimestre["Mes"] == mes]

        gdf_mes = gdf_ccaa.merge(
            datos_mes[["acom_name", "Recuperados_miles"]],
            on="acom_name",
            how="left"
        )

        gdf_mes.plot(
            column="Recuperados_miles",
            ax=ax,
            cmap=cmap,
            norm=norm_rec,
            edgecolor="black",
            linewidth=0.4
        )

        ax.set_title(mes)
        ax.set_axis_off()

    sm2 = ScalarMappable(norm=norm_rec, cmap=cmap)
    sm2.set_array([])

    cbar2 = fig2.colorbar(
        sm2,
        ax=axes2.ravel().tolist(),
        fraction=0.035,
        pad=0.08
    )
    cbar2.set_label("Casos recuperados (miles)")

    # Ticks cada 10: 0, 10, 20, 30, 40, 50
    ticks_rec = np.arange(0, max_val_rec + 1, 10)
    cbar2.set_ticks(ticks_rec)
    cbar2.set_ticklabels([str(int(t)) for t in ticks_rec])

    fig2.suptitle(
        "Casos recuperados de COVID por comunidad autónoma\n"
        "España, primer trimestre de 2021",
        y=0.94
    )

    plt.tight_layout(rect=[0, 0, 0.86, 0.9])

    salida_rec = os.path.join(script_dir, "grafico_ejercicio5_7_mapa_recuperados.png")
    fig2.savefig(salida_rec, dpi=200)


if __name__ == "__main__":
    main()