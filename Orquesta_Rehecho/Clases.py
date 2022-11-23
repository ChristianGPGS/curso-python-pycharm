import utils.logging_orquesta as log
from abc import ABC, abstractmethod
from utils.general_utils import generar_aleatorio_booleano


def decorador_logs_afinar(afinar):
    def decorador_logs_prints(*args):
        log.debug("Ejecutando el metodo afinar")
        afinar()
        log.debug("Terminado el metodo afinar")


def decorador_logs_tocar(tocar):
    def decorador_logs_prints(*args):
        log.debug("Ejecutando el metodo tocar")
        tocar()
        log.debug("Terminado el metodo tocar")


class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    @abstractmethod
    def afinar(self):
        pass


    @abstractmethod
    def tocar_instrumento(self):
        pass


class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, num_cuerdas):
        super().__init__(nombre=nombre, tipo=tipo)
        self.num_cuerdas = num_cuerdas


class Guitarra_Electrica(Guitarra):
    def __init__(self, nombre, tipo, num_cuerdas, potencia):
        super().__init__(nombre=nombre, tipo=tipo, num_cuerdas=num_cuerdas)
        self.potencia = potencia

    def afinar(self):
        esta_afinado = False
        while esta_afinado == False:
            afinar = random.randint(0, 1)
            if afinar == 1:
                esta_afinado = True
            else:
                log.debug("No afinado")
                raise No_Afinado_Exception('El instrumento {} no está afinado'.format(self.nombre))
        return "El instrumento esta afinado"

    def tocar_instrumento(self):
        log.info("Tocamos el instrumento {}".format(self.nombre))


class Piano(Instrumento):
    def __init__(self, nombre, tipo, num_teclas):
        super().__init__(nombre=nombre, tipo=tipo)
        self.num_teclas = num_teclas

    def afinar(self):
        esta_afinado = False
        while esta_afinado == False:
            afinar = random.randint(0, 1)
            if afinar == 1:
                esta_afinado = True
            else:
                log.debug("No afinado")
                raise No_Afinado_Exception('El instrumento {} no está afinado'.format(self.nombre))
        return "El instrumento esta afinado"

    def tocar_instrumento(self):
        log.info("Tocamos el instrumento {}".format(self.nombre))


class Tambor(Instrumento):
    def __init__(self, nombre, tipo, tamanio):
        super().__init__(nombre=nombre, tipo=tipo)

    def aporrear(self):
        log.info("Aporreo como un makako")

    def afinar(self):
        esta_afinado = False
        while esta_afinado == False:
            afinar = random.randint(0, 1)
            if afinar == 1:
                esta_afinado = True
            else:
                log.debug("No afinado")
                raise No_Afinado_Exception('El instrumento {} no está afinado'.format(self.nombre))
        return "El instrumento esta afinado"


