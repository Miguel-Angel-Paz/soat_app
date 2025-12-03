import pandas as pd

def leer_base(ruta_excel):
    """
    Lee un archivo Excel con columnas: nombre, telefono, fecha_compra.
    Retorna un DataFrame.
    """

    try:
        df = pd.read_excel(ruta_excel)
        return df
    except Exception as e:
        print(f"Error leyendo el archivo: {e}")
        return None

