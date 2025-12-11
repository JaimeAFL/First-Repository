import pandas

def main():

    ruta_csv = "/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/datos_covid/COVID_01-01-2021.csv"
    dataframe = pandas.read_csv(ruta_csv)

    print("Información del DataFrame (ENERO) ")
    print("---------------------------------")
    print(dataframe.info())
    print()

    print("Datos faltantes por columna")
    print("---------------------------")
    print(dataframe.isna().sum())
    print()

    print("                                                            Primeras 5 filas del DataFrame")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(dataframe.head())

if __name__ == "__main__":
    main()   