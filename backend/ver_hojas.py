import pandas as pd

xls = pd.ExcelFile("datos/BASE DE DATOS DOCUMENTAL PESV - 2023 (3).xlsx")
print(xls.sheet_names)
