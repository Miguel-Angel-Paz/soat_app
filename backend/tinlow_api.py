def llamar_tinlow(telefono, mensaje):
    """
    Función donde se integrará Tinlow.
    Tinlow SOLO debe llamar a personas con estado:
        - 'PRÓXIMO A VENCER'
        - 'VENCIDO'
    Nunca llamar a los que están 'VIGENTE'.
    """

    print(f"Llamando a {telefono} con mensaje:\n{mensaje}\n")


def enviar_alertas(lista_alertas):
    """
    Envía alertas SOLO a los estados permitidos.
    Lógica clara para Tinlow:
        - Si estado == VIGENTE → NO se llama.
        - Si estado == PRÓXIMO A VENCER → llamada preventiva.
        - Si estado == VENCIDO → llamada urgente.
    """

    for alerta in lista_alertas:
        estado = alerta["estado"]

        # OMITIR VIGENTES
        if estado == "VIGENTE":
            continue

        # MENSAJE PERSONALIZADO
        if estado == "PRÓXIMO A VENCER":
            mensaje = (
                f"Hola {alerta['nombre']}, tu SOAT está PRÓXIMO A VENCER.\n"
                f"Te quedan {alerta['dias_restantes']} días para renovarlo."
            )

        elif estado == "VENCIDO":
            mensaje = (
                f"Hola {alerta['nombre']}, tu SOAT está VENCIDO.\n"
                f"Por favor renuévalo lo antes posible para evitar multas."
            )

        # LLAMADA A TINLOW
        llamar_tinlow(alerta["telefono"], mensaje)

