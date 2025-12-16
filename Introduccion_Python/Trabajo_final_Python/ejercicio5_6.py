
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    # Carpeta donde está ESTE archivo
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Rutas de los CSV dentro de datos_covid
    ruta_enero = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")
    ruta_febrero = os.path.join(script_dir, "datos_covid", "COVID_01-02-2021.csv")
    ruta_marzo = os.path.join(script_dir, "datos_covid", "COVID_01-03-2021.csv")

    # DataFrames de cada archivo CSV
    df_enero = pd.read_csv(ruta_enero)
    df_febrero = pd.read_csv(ruta_febrero)
    df_marzo = pd.read_csv(ruta_marzo)

    # Totales mundiales por mes
    totales_enero = df_enero[["Confirmed", "Deaths", "Recovered"]].sum()
    totales_febrero = df_febrero[["Confirmed", "Deaths", "Recovered"]].sum()
    totales_marzo = df_marzo[["Confirmed", "Deaths", "Recovered"]].sum()

    # DataFrame resumen
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

    # Formato largo para seaborn
    datos_plot = resumen_mensual.melt(
        id_vars="Mes",
        value_vars=["Confirmados", "Fallecidos", "Recuperados"],
        var_name="Tipo_caso",
        value_name="Casos"
    )

    # Escalar a millones de casos
    datos_plot["Casos_millones"] = datos_plot["Casos"] / 1_000_000

    # Estilo de seaborn
    sns.set_theme(style="whitegrid")

    # Gráfico de líneas (en millones)
    plt.figure(figsize=(10, 6))
    ax = sns.lineplot(
        data=datos_plot,
        x="Mes",
        y="Casos_millones",
        hue="Tipo_caso",
        marker="o"
    )

    ax.set_title("Evolución COVID primer trimestre 2021")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Número de casos (millones)")

    plt.tight_layout()

    # Guardar el gráfico junto al script
    ruta_salida = os.path.join(script_dir, "grafico_ejercicio5_6.png")
    plt.savefig(ruta_salida, dpi=150)


if __name__ == "__main__":
    main()