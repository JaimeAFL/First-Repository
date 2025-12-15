# ejercicio5_7.py

import pandas as pd
import seaborn as sns


def resumen_spain_por_mes(df, nombre_mes):
    """
    Filtra España, agrupa por provincia y devuelve un dataframe con:
    Province_State, Confirmed, Recovered, Mes
    """
    df_spain = df[df["Country_Region"] == "Spain"].copy()

    # Eliminar filas sin provincia (país agregado) o provincia 'Unknown'
    df_spain = df_spain[df_spain["Province_State"].notna()]
    df_spain = df_spain[df_spain["Province_State"] != "Unknown"]

    # Agrupar por provincia y sumar casos confirmados y recuperados
    resumen = (
        df_spain
        .groupby("Province_State")[["Confirmed", "Recovered"]]
        .sum()
        .reset_index()
    )

    # Añadir columna del mes
    resumen["Mes"] = nombre_mes
    return resumen


def main():
    # Rutas de los CSV
    ruta_enero = "datos/COVID_01-01-2021.csv"
    ruta_febrero = "datos/COVID_01-02-2021.csv"
    ruta_marzo = "datos/COVID_01-03-2021.csv"

    # DataFrames de cada archivo
    df_enero = pd.read_csv(ruta_enero)
    df_febrero = pd.read_csv(ruta_febrero)
    df_marzo = pd.read_csv(ruta_marzo)

    # Resumen por provincias de España en cada mes
    resumen_enero = resumen_spain_por_mes(df_enero, "Enero")
    resumen_febrero = resumen_spain_por_mes(df_febrero, "Febrero")
    resumen_marzo = resumen_spain_por_mes(df_marzo, "Marzo")

    # Unir los tres meses en un solo dataframe
    resumen_trimestre = pd.concat(
        [resumen_enero, resumen_febrero, resumen_marzo],
        ignore_index=True
    )

    # Pasar a formato largo para poder diferenciar Confirmados / Recuperados en el gráfico
    datos_plot = resumen_trimestre.melt(
        id_vars=["Province_State", "Mes"],
        value_vars=["Confirmed", "Recovered"],
        var_name="Tipo_caso",
        value_name="Casos"
    )

    # Asegurar que los meses salen en orden correcto
    orden_meses = ["Enero", "Febrero", "Marzo"]
    datos_plot["Mes"] = pd.Categorical(datos_plot["Mes"],
                                       categories=orden_meses,
                                       ordered=True)

    # Estilo de seaborn
    sns.set_theme(style="whitegrid")

    # Opción elegida: dos gráficos (uno Confirmados, otro Recuperados),
    # con una línea por provincia en cada gráfico.
    grafico = sns.relplot(
        data=datos_plot,
        kind="line",
        x="Mes",
        y="Casos",
        hue="Province_State",
        col="Tipo_caso",      # una columna para Confirmed y otra para Recovered
        marker="o",
        height=5,
        aspect=1.4
    )

    grafico.set_axis_labels("Mes", "Número de casos")
    grafico.fig.suptitle(
        "Evolución de casos confirmados y recuperados de COVID\n"
        "Provincias de España, primer trimestre 2021",
        y=1.03
    )


if __name__ == "__main__":
    main()
