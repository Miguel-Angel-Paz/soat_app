# 1.El "Corazón" del Negocio:
# Este módulo ya lo explicamos, pero lo importante es que no depende de nadie. Es puro cálculo matemático.
# Lógica profesional: Usa timedelta(days=365) para proyectar el futuro. Es perfecto porque separa la fecha de hoy (datetime.now()) del dato del cliente.


from datetime import datetime, timedelta

# Ideal para tests automáticos TENERLO EN CUENTA MAS ADELANTE
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


