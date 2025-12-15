
import pandas
import seaborn

def main():

    ruta_csv = "datos/COVID_01-01-2021.csv"
    df = pandas.read_csv(ruta_csv)

    resumen_paises = (
        df.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]]
        .sum()
        .reset_index())

    paises_filtrados = resumen_paises[resumen_paises["Deaths"] < 150]

    datos_plot = paises_filtrados.melt(
        id_vars="Country_Region",
        value_vars=["Confirmed", "Deaths", "Recovered"],
        var_name="Tipo_caso",
        value_name="Casos")

    seaborn.set_theme(style="whitegrid")

    grafico = seaborn.catplot(
        data=datos_plot,
        kind="bar",
        x="Country_Region",
        y="Casos",
        hue="Tipo_caso",
        height=6,
        aspect=2)

    grafico.set_axis_labels("País", "Número de casos")
    grafico.set_xticklabels(rotation=45)
    grafico.fig.suptitle(
        "Casos confirmados, fallecidos y recuperados\n"
        "(Países con menos de 150 fallecidos, enero 2021)",
        y=1.03)

if __name__ == "__main__":
    main()