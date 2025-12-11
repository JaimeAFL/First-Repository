import pandas

def main():

    ruta_csv = "/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/datos_covid/COVID_01-01-2021.csv"
    dataframe = pandas.read_csv(ruta_csv)

    resumen_paises = (
        dataframe.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]]
        .sum())

    top_10 = (
        resumen_paises
        .sort_values(by="Confirmed", ascending=False)
        .head(10)
        .reset_index())

    print("=== 10 países con más casos confirmados (enero 2021) ===")
    print(top_10)

if __name__ == "__main__":
    main()