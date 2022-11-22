# Clase donde se inicia el programa
import utils.logging_bar as log
import persona as p
from temperature_exception import toocold_exception, toohot_exception


class Bar():
    cliente1 = p.Cliente("Cliente1", "Cliente1")

    camarero1 = p.Camarero("Camarero1", "Camarero1")
    taza_cafe = camarero1.servir_taza_cafe()
    try:
        cliente1.tomar_taza_cafe(taza_cafe.temperatura)
    except toohot_exception as e:
        log.error(e.mensaje)
    except toocold_exception as e:
        log.error(e.mensaje)
    except Exception as e:
        print(f'Exception - Ocurrió un error: {e} , {type(e)}')
    else:
        log.info("El cafe esta perfecto, su temperatura es de {}".format(taza_cafe.temperatura))
