# Clase donde se inicia el programa
import utils.logging_bar as log
import persona as p
import temperature_exception


class Bar():
    cliente1 = p.Cliente("Cliente1", "Cliente1")

    camarero1 = p.Camarero("Camarero1", "Camarero1")
    taza_cafe = camarero1.servir_taza_cafe()
    try:
        cliente1.tomar_taza_cafe(taza_cafe.temperatura)
    except Exception as e:
        print(f'Exception - Ocurrió un error: {e} , {type(e)}')
