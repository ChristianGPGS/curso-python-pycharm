class afinar_exception(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class no_afinado_exception(afinar_exception):
    def __init__(self, mensaje):
        afinar_exception.__init__(self, mensaje=mensaje)
