import pandas

def main():

    ruta_csv = "/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/datos_covid/COVID_01-01-2021.csv"
    dataframe = pandas.read_csv(ruta_csv)

    sin_recuperados = dataframe[dataframe["Recovered"].fillna(0) == 0]

    sin_recuperados = sin_recuperados[sin_recuperados["Province_State"].notna()]

    provincias_paises = (
        sin_recuperados[["Province_State", "Country_Region"]]
        .drop_duplicates()
        .reset_index(drop=True))

    print("=== Provincias sin casos de pacientes recuperados (enero 2021) ===")
    print(provincias_paises)


if __name__ == "__main__":
    main()
