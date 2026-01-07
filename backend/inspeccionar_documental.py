#Este archivo lo hago solo para ver el Problema de "FECHA" que no entiendo, 
# pero despues entndi que habia filas ocultas en la parte superior de los encabezados


import pandas as pd

df = pd.read_excel(
    "../datos/BASE DE DATOS DOCUMENTAL PESV - 2023 (3).xlsx",
    sheet_name="SEPTIEMBRE 2023"
)

print("Columnas reales que leyó pandas:")
for col in df.columns:
    print(f"- '{col}'")