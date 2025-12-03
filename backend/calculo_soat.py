from datetime import datetime, timedelta

def calcular_estado(fecha_compra):
    """
    Calcula el estado del SOAT basado en la fecha de compra.
    Retorna: ("ESTADO", dias_restantes)
    Estados posibles:
        - VIGENTE (más de 30 días)
        - PRÓXIMO A VENCER (entre 1 y 30 días)
        - VENCIDO (0 días o negativos)
    """

    hoy = datetime.now().date()
    dias_vigencia = 365
    fecha_vencimiento = fecha_compra + timedelta(days=dias_vigencia)

    dias_restantes = (fecha_vencimiento - hoy).days

    if dias_restantes > 30:
        return "VIGENTE", dias_restantes

    elif 0 < dias_restantes <= 30:
        return "PRÓXIMO A VENCER", dias_restantes

    else:
        return "VENCIDO", dias_restantes

