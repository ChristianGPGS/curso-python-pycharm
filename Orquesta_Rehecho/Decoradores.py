import utils.logging_orquesta as log


def decorador_logs (funcion_a_decorar_b):
    def funcion_decorador_c(*args):
        log.debug(f"Antes ejecución método {funcion_a_decorar_b.__name__}")
        funcion_a_decorar_b(*args)
        log.debug(f"Después ejecución método {funcion_a_decorar_b.__name__}")

    return funcion_decorador_c