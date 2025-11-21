import pandas as pd
import matplotlib.pyplot as plt

def graficar_desviaciones(nombre_archivo):
    try:
        df = pd.read_csv(nombre_archivo)
        columnas = ["CP1", "CP2", "CP3", "NF"]

        for col in columnas:
            if col not in df.columns:
                print(f"Columna no encontrada: {col}")
                return

        desviaciones = df[columnas].std()

        plt.bar(desviaciones.index, desviaciones.values)
        plt.xlabel("Categorías")
        plt.ylabel("Desviación Estándar")
        plt.title("Desviaciones Estándar: CP1, CP2, CP3 y NF")
        plt.tight_layout()

        plt.savefig("Figuras/Desviaciones.png")

        plt.show()

    except Exception as e:
        print("Error al procesar el archivo:", e)


graficar_desviaciones("Figuras/quiz.csv")
plt.savefig("Figuras/Desviacion.png")
