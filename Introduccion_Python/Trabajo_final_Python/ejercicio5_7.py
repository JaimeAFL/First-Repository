# ejercicio5_7.py

import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def resumen_spain_por_mes(df, nombre_mes):
    """Devuelve totales Confirmed/Recovered por provincia de España para un mes."""
    df_spain = df[df["Country_Region"] == "Spain"].copy()

    # Quitar filas sin provincia o con provincia "Unknown"
    df_spain = df_spain[df_spain["Province_State"].notna()]
    df_spain = df_spain[df_spain["Province_State"] != "Unknown"]

    resumen = (
        df_spain
        .groupby("Province_State")[["Confirmed", "Recovered"]]
        .sum()
        .reset_index()
    )
    resumen["Mes"] = nombre_mes
    return resumen


def main():
    # Carpeta donde está ESTE archivo
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Rutas CSV
    ruta_enero = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")
    ruta_febrero = os.path.join(script_dir, "datos_covid", "COVID_01-02-2021.csv")
    ruta_marzo = os.path.join(script_dir, "datos_covid", "COVID_01-03-2021.csv")

    # DataFrames
    df_enero = pd.read_csv(ruta_enero)
    df_febrero = pd.read_csv(ruta_febrero)
    df_marzo = pd.read_csv(ruta_marzo)

    # Resúmenes por mes
    resumen_enero = resumen_spain_por_mes(df_enero, "Enero")
    resumen_febrero = resumen_spain_por_mes(df_febrero, "Febrero")
    resumen_marzo = resumen_spain_por_mes(df_marzo, "Marzo")

    resumen_trimestre = pd.concat(
        [resumen_enero, resumen_febrero, resumen_marzo],
        ignore_index=True
    )

    # Formato largo
    datos_plot = resumen_trimestre.melt(
        id_vars=["Province_State", "Mes"],
        value_vars=["Confirmed", "Recovered"],
        var_name="Tipo_caso",
        value_name="Casos"
    )

    # Casos en miles para que la escala sea legible
    datos_plot["Casos_miles"] = datos_plot["Casos"] / 1_000

    # Orden de meses
    meses = ["Enero", "Febrero", "Marzo"]
    datos_plot["Mes"] = pd.Categorical(datos_plot["Mes"],
                                       categories=meses,
                                       ordered=True)

    # Valor máximo para compartir escala entre los 3 mapas
    max_val = datos_plot["Casos_miles"].max()

    sns.set_theme(style="whitegrid")

    # Figura con 3 mapas de calor (uno por mes)
    fig, axes = plt.subplots(1, 3, figsize=(18, 10), sharey=True)

    # Ticks de la barra de color (en miles)
    ticks = [20, 40, 60, 80, 100]

    for ax, mes in zip(axes, meses):
        datos_mes = datos_plot[datos_plot["Mes"] == mes]

        # Matriz: filas = provincias, columnas = Confirmados / Recuperados
        matriz = (
            datos_mes.pivot(index="Province_State",
                            columns="Tipo_caso",
                            values="Casos_miles")
            .sort_index()
        )

        sns.heatmap(
            matriz,
            ax=ax,
            cmap="Reds",
            vmin=0,
            vmax=max_val,
            cbar_kws={
                "label": "Número de casos (miles)",
                "ticks": ticks
            }
        )

        ax.set_title(f"{mes}")
        ax.set_xlabel("Tipo de caso")
        ax.set_ylabel("Provincia")

        # Etiquetas legibles
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="x", rotation=0)

    fig.suptitle(
        "Mapas de calor de casos confirmados y recuperados de COVID\n"
        "Provincias de España, primer trimestre 2021",
        y=0.98
    )

    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Guardar imagen
    salida = os.path.join(script_dir, "grafico_ejercicio5_7_heatmaps.png")
    plt.savefig(salida, dpi=150)
    print(f"Gráfico guardado en: {salida}")


if __name__ == "__main__":
    main()
