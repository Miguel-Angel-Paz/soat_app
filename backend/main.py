from lector_bd import leer_y_cruzar_bases
from generador_alertas import generar_alertas
from tinlow_api import enviar_alertas

def run():
    print("--- INICIANDO SOAT_APP 2025 ---")

    try:
        # 1. Leer, limpiar y cruzar datos
        datos = leer_y_cruzar_bases()

        if datos is None or datos.empty:
            print("⚠ No hay datos válidos para procesar")
            return

        # 2. Generar alertas SOAT
        lista_alertas = generar_alertas(datos)

        # 3. Enviar alertas (Tinlow)
        enviar_alertas(lista_alertas)

        print("--- PROCESO COMPLETADO EXITOSAMENTE ---")

    except Exception as e:
        print("❌ Error crítico en la ejecución:", e)


if __name__ == "__main__":
    run()
