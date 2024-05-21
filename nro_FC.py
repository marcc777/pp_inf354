import pandas as pd
import easygui as gui

def cargar_datos_csv(nombreArchivo, codificaciones=['utf-8', 'latin1', 'iso-8859-1']):

    # es como un foreach:
    for x in codificaciones:
        try:
            df = pd.read_csv(nombreArchivo, encoding = x)
            return df
        except UnicodeDecodeError:
            continue
    return None

# Intenta cargar el dataset con diferentes codificaciones
nombreArchivo = 'netflix_titles.csv'
df = cargar_datos_csv(nombreArchivo)

# Muestra el número de filas y columnas del DataFrame si se ha cargado correctamente
if df is not None:
    num_filas = df.shape[0]
    num_columnas = df.shape[1]
    mensaje = f"Número de columnas = {num_columnas}, Número de filas = {num_filas}"
    gui.msgbox(mensaje, title="nro de filas, nro de columnas")
else:
    gui.msgbox("Error al cargar el archivo CSV con las codificaciones disponibles.", title="Error")

