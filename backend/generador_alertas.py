# 3.El "Cerebro Operativo":
# Aquí conectas la tabla de datos con el cálculo.
# for index, row in df.iterrows():: Esto recorre tu Excel fila por fila.
# resultados.append({...}): Construye una lista de "paquetes de información" (diccionarios) que contienen todo lo necesario para que Tinlow sepa a quién llamar y qué decir.

from calculo_soat import calcular_estado

def generar_alertas(df):
    """
    Genera una lista de alertas con la siguiente estructura:
    {
        nombre: str,
        telefono: str/int,
        fecha_compra: date,
        estado: str,
        dias_restantes: int
    }
    """

    resultados = []

    for index, row in df.iterrows():
        fecha_compra = row["fecha_compra"].date()
        estado, dias_restantes = calcular_estado(fecha_compra)

        resultados.append({
            "nombre": row["nombre"],
            "telefono": row["telefono"],
            "fecha_compra": fecha_compra,
            "estado": estado,
            "dias_restantes": dias_restantes
        })

    return resultados

