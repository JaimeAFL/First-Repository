# ejercicio5_6.py

import pandas as pd
import numpy as np
import seaborn as sns


def main():
    # Rutas de los CSV (carpeta "datos" según tu organización)
    ruta_enero = "/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/datos_covid/COVID_01-01-2021.csv"
    ruta_febrero = "/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/datos_covid/COVID_01-02-2021.csv"
    ruta_marzo = "/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/datos_covid/COVID_01-03-2021.csv"

    # Crear un dataframe para cada archivo CSV
    df_enero = pd.read_csv(ruta_enero)
    df_febrero = pd.read_csv(ruta_febrero)
    df_marzo = pd.read_csv(ruta_marzo)

    # Calcular totales mundiales por mes (Confirmados, Fallecidos, Recuperados)
    totales_enero = df_enero[["Confirmed", "Deaths", "Recovered"]].sum()
    totales_febrero = df_febrero[["Confirmed", "Deaths", "Recovered"]].sum()
    totales_marzo = df_marzo[["Confirmed", "Deaths", "Recovered"]].sum()

    # Crear dataframe resumen (filas = meses, columnas = tipos de casos)
    resumen_mensual = pd.DataFrame({
        "Mes": np.array(["Enero", "Febrero", "Marzo"]),
        "Confirmados": np.array([
            totales_enero["Confirmed"],
            totales_febrero["Confirmed"],
            totales_marzo["Confirmed"],
        ]),
        "Fallecidos": np.array([
            totales_enero["Deaths"],
            totales_febrero["Deaths"],
            totales_marzo["Deaths"],
        ]),
        "Recuperados": np.array([
            totales_enero["Recovered"],
            totales_febrero["Recovered"],
            totales_marzo["Recovered"],
        ]),
    })

    # Pasar a formato largo para usar seaborn (Mes, Tipo_caso, Casos)
    datos_plot = resumen_mensual.melt(
        id_vars="Mes",
        value_vars=["Confirmados", "Fallecidos", "Recuperados"],
        var_name="Tipo_caso",
        value_name="Casos"
    )

    # Configurar estilo de seaborn
    sns.set_theme(style="whitegrid")

    # Gráfico de líneas:
    # - Eje X: meses
    # - Eje Y: número de casos
    # - Hue: tipo de caso (Confirmados / Fallecidos / Recuperados)
    ax = sns.lineplot(
        data=datos_plot,
        x="Mes",
        y="Casos",
        hue="Tipo_caso",
        marker="o"
    )

    # Título y etiquetas de ejes según el enunciado
    ax.set_title("Evolución COVID primer trimestre 2021")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Número de casos")


if __name__ == "__main__":
    main()
