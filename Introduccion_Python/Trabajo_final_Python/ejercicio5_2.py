import pandas

def main():

    ruta_csv = "/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/datos_covid/COVID_01-01-2021.csv"
    dataframe = pandas.read_csv(ruta_csv)

    resumen_paises = (
        dataframe.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered", "Active"]]
        .sum()
        .reset_index()
    )

    print("            Totales de COVID por país (enero 2021)")
    print("--------------------------------------------------------------")
    print(resumen_paises)

if __name__ == "__main__":
    main()