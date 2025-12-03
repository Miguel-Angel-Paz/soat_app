from lector_bd import leer_base
from generador_alertas import generar_alertas
from tinlow_api import enviar_alertas

def run():
    print("Cargando base de SOATs...")
    datos = leer_base("soats.xlsx")

    print("Generando alertas...")
    lista_alertas = generar_alertas(datos)

    print("Enviando alertas a Tinlow (solo vencidos y próximos a vencer)...")
    enviar_alertas(lista_alertas)

if __name__ == "__main__":
    run()

