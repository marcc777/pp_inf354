import numpy as np
from sklearn.impute import SimpleImputer as si

# pip install scikit-learn

# Creamos un SimpleImputer con estrategia de imputación media para valores NaN
prepro = si(missing_values=np.nan, strategy="mean")

# Creamos un array numpy con valores, incluidos algunos NaN
x1 = np.array([
    [1, 2, 3],
    [4, np.nan, 6],
    [np.nan, 8, np.nan]
])

# Imprimimos el array original x1
print("Array original:")
print(x1)

# Aplicamos el SimpleImputer a x1, ajustando y transformando los datos
x2 = prepro.fit_transform(x1)

# Imprimimos el array transformado x2, donde NaNs son reemplazados por la media de cada columna
print("\nArray transformado con SimpleImputer:")
print(x2)
