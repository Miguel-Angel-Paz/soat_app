import pandas as pd

df = pd.read_excel(
    "../datos/BASE DE DATOS DOCUMENTAL PESV - 2023 (3).xlsx",
    sheet_name="SEPTIEMBRE 2023",
    header=None
)

print(df.head(15))


