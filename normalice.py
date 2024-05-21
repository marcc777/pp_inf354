import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Paso 1: Crear y visualizar el conjunto de datos original
data = {
    'Edad': [25, 30, 40, 50, 60, 70],
    'Ingreso': [50000, 70000, 100000, 120000, 90000, 30000]
}
df = pd.DataFrame(data)

print("Datos originales:")
print(df)

# Paso 2: Normalizar los datos
scaler = MinMaxScaler()
df_normalizado = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("\nDatos normalizados:")
print(df_normalizado)
