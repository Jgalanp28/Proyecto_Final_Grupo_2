import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

archivo = 'Figuras/quiz.csv'
df = pd.read_csv(archivo)

columna_p3 = df.iloc[:,3]
def limpiar_valor(valor):
    try:
        if isinstance(valor, str):
            valor = valor.replace(",", ".")
            valor = valor.strip()
            if "," in valor and "." in valor:
                partes = valor.split(",")
                if len(partes) == 2:
                    valor = partes[0] + "." + partes[1]
        return float(valor)
    except (ValueError, AttributeError):
        return np.nan

valores_limpios_p3 = columna_p3.apply(limpiar_valor)
valor_correcto_p3 = (2 * df["n"] * 100 + 2).round(2)
df["CP3"] = np.where(valores_limpios_p3 == valor_correcto_p3, 5, 1)


df["NF"] = ((df["CP1"] + df["CP2"] + df["CP3"]) / 3).round(2)


plt.figure(figsize=(10, 6))


percentiles = [i/10 for i in range(1, 10)]
valores_percentiles = df["NF"].quantile(percentiles)


barras = plt.bar([f"P{int(p*100)}" for p in percentiles],
                 valores_percentiles.values,
                 color='skyblue',
                 edgecolor='navy')

plt.xlabel('Percentiles')
plt.ylabel('Valor de NF')
plt.title('Percentiles de NF (10, 20, 30, ..., 90)')
plt.grid(axis='y', alpha=0.3)

for barra in barras:
    height = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom')

plt.tight_layout()


plt.savefig('Percentiles.png', dpi=300)
plt.show()