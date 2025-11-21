import pandas as pd
import matplotlib.pyplot as plt

def graficar_promedios(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        columnas = ["CP1", "CP2", "CP3", "NF"]

        for col in columnas:
            if col not in df.columns:
                print(f"Columna no encontrada: {col}")
                return

        promedios = df[columnas].mean()

        plt.bar(promedios.index, promedios.values)
        plt.xlabel("Categorías")
        plt.ylabel("Promedio")
        plt.title("Promedios: CP1, CP2, CP3 y NF")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error al procesar el archivo:", e)

graficar_promedios("Figuras/quiz.csv")
plt.savefig("Figuras/promedios.png")

