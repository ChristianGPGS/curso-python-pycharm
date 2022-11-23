def decorador_logs(metodo):
    def decorador_logs_prints():
        log.debug(f"Ejecutando el metodo {metodo.__name__}:")
        metodo()
        log.debug(f"Terminado el metodo {metodo.__name__}")
