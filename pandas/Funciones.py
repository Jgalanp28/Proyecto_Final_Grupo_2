import pandas as pd

def promedios(nombre_archivo, nombre_columna):
    try:
        df = pd.read_csv(nombre_archivo)
        if nombre_columna not in df.columns:
            print("Error al procesar la columna")
            return None
        promedio = df[nombre_columna].mean()      
        return promedio
    except Exception as e:
        print("Error al procesar la columna")
        return None