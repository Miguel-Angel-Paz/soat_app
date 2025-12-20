# Rol: Área de Datos / ETL


import pandas as pd
import re

# -------------------------
# Limpieza de teléfono
# -------------------------
def limpiar_telefono(tel):
    if pd.isna(tel):
        return ""

    tel = str(tel)
    tel = tel.split('-')[0]          # Quita extensión
    tel = re.sub(r'\D', '', tel)     # Solo números
    tel = tel.lstrip('0')            # Quita ceros iniciales

    return tel if len(tel) == 10 else ""


# -------------------------
# Lectura, limpieza y cruce
# -------------------------
def leer_y_cruzar_bases():
    try:
        # Leer archivos y hojas específicas
        banco = pd.read_excel(
            "Base Banco completa SB Jun 2024.xlsx",
            sheet_name="Emp_Activos 30 Jun"
        )

        documental = pd.read_excel(
            "BASE DE DATOS DOCUMENTAL PESV - 2023 (3).xlsx",
            sheet_name="SEPTIEMBRE 2023"
        )

        # -------------------------
        # Limpieza base documental
        # -------------------------
        documental["nombre"] = documental["COLABORADOR"].str.strip()

        documental["fecha_compra"] = pd.to_datetime(
            documental["FECHA SOAT"],
            errors="coerce"
        )

        # -------------------------
        # Limpieza base banco
        # -------------------------
        banco["telefono"] = banco["TELEFONO"].apply(limpiar_telefono)
        banco = banco[banco["telefono"] != ""]

        # -------------------------
        # Cruce por CEDULA
        # -------------------------
        df_final = documental.merge(
            banco[["CEDULA", "telefono"]],
            on="CEDULA",
            how="left"
        )

        # -------------------------
        # Limpieza final
        # -------------------------
        df_final = df_final.dropna(subset=["fecha_compra"])

        return df_final[["CEDULA", "nombre", "telefono", "fecha_compra"]]

    except FileNotFoundError as e:
        print("❌ Archivo Excel no encontrado:", e)
        return None

    except KeyError as e:
        print("❌ Columna faltante en el Excel:", e)
        return None

    except Exception as e:
        print("❌ Error inesperado en lector_bd:", e)
        return None
