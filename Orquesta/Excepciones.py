import utils.logging_orquesta as log

class No_Afinado_Exception(Exception):
    def __init__(self,mensaje):
        self.mensaje =mensaje