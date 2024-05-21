"""
import pandas as pd

# Carga el dataset
# df = pd.read_csv('/kaggle/input/netflix-movies-and-tv-shows/netflix_titles.csv')
df = pd.read_csv('netflix_titles.csv')


# Muestra el número de filas y columnas
df.shape
"""


"""
import pandas as pd

# Carga el dataset
# Prueba con diferentes codificaciones
df = pd.read_csv('netflix_titles.csv', encoding='latin1')  # O usa 'iso-8859-1' o 'cp1252'

# Muestra el número de filas y columnas
print(df.shape)
"""








"""
import pandas as pd

# Por defecto, pandas.read_csv usa la codificación UTF-8

# Intenta cargar el archivo CSV con diferentes codificaciones si es necesario
try:
    df = pd.read_csv('netflix_titles.csv', encoding='latin1')
except UnicodeDecodeError:
    df = pd.read_csv('netflix_titles.csv', encoding='iso-8859-1')

# Muestra el número de filas y columnas del DataFrame
num_filas = df.shape[0]
num_columnas = df.shape[1]

print(f"Número de filas = {num_filas}, Número de columnas = {num_columnas}")
"""








import pandas as pd

# Carga el dataset

try:
    df = pd.read_csv('netflix_titles.csv')
except:
    print("Error de codificacion")
    try:
        df = pd.read_csv('netflix_titles.csv', encoding='latin1')
    except UnicodeDecodeError:
        df = pd.read_csv('netflix_titles.csv', encoding='iso-8859-1')


    # Muestra el número de filas y columnas del DataFrame
    num_filas = df.shape[0]
    num_columnas = df.shape[1]
    print(f"Número de filas = {num_filas}, Número de columnas = {num_columnas}")
        


# Muestra el número de filas y columnas
# df.shape
