
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    # Carpeta donde está ESTE archivo (ejercicio5_5.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Ruta al CSV dentro de la carpeta datos_covid
    ruta_csv = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")
    df = pd.read_csv(ruta_csv)

    # Agrupar por país y sumar casos confirmados, fallecidos y recuperados
    resumen_paises = (
        df.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]]
        .sum()
        .reset_index()
    )

    # Filtrar solo los países con menos de 150 fallecidos
    paises_filtrados = resumen_paises[resumen_paises["Deaths"] < 150]

    # Para que el gráfico sea legible, nos quedamos con los 15 países
    # con más casos confirmados dentro de ese filtro
    paises_filtrados = paises_filtrados.sort_values(
        by="Confirmed",
        ascending=False
    )    

    # Pasar a formato largo SOLO con Confirmados y Recuperados
    datos_plot = paises_filtrados.melt(
        id_vars="Country_Region",
        value_vars=["Confirmed", "Recovered"],
        var_name="Tipo_caso",
        value_name="Casos"
    )

    # Estilo de seaborn
    sns.set_theme(style="whitegrid")

    # Crear figura y eje con matplotlib, y dibujar con seaborn
    plt.figure(figsize=(18, 6))
    ax = sns.barplot(
        data=datos_plot,
        x="Country_Region",
        y="Casos",
        hue="Tipo_caso"
    )

    # Títulos y etiquetas
    ax.set_title(
        "Casos confirmados y recuperados\n"
        "(Países con menos de 150 fallecidos, enero 2021)"
    )
    ax.set_xlabel("País")
    ax.set_ylabel("Número de casos")

    # Rotar etiquetas del eje X para que no se solapen
    plt.xticks(rotation=45, ha="right")

    # Ajustar márgenes
    plt.tight_layout()

    # Guardar el gráfico en la MISMA carpeta que este script
    ruta_salida = os.path.join(script_dir, "grafico_ejercicio5_5.png")
    plt.savefig(ruta_salida, dpi=150)


if __name__ == "__main__":
    main()