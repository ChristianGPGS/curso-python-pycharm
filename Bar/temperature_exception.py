class temperature_exception(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class toohot_exception(temperature_exception):
    def __init__(self, mensaje):
        temperature_exception.__init__(self, mensaje=mensaje)


class toocold_exception(temperature_exception):
    def __init__(self, mensaje):
        temperature_exception.__init__(self, mensaje=mensaje)
