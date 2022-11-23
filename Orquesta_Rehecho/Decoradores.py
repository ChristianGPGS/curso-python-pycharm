def decorador_logs(metodo):
    def decorador_logs_prints(*args):
        log.debug(f"Ejecutando el metodo {metodo.__name__}:")
        metodo(*args)
        log.debug(f"Terminado el metodo {metodo.__name__}")
