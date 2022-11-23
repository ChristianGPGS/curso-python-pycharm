import utils.logging_orquesta as log
from abc import ABC
import random

def decorador_logs_afinar(afinar):
    def decorador_logs_prints():
        log.debug("Ejecutando el metodo afinar")
        afinar()
        log.debug("Terminado el metodo afinar")

def decorador_logs_tocar(tocar):
    def decorador_logs_prints():
        log.debug("Ejecutando el metodo tocar")
        tocar()
        log.debug("Terminado el metodo tocar")

class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    # añadir decorador

    @decorador_logs_afinar
    def afinar(self):
        esta_afinado = False
        while esta_afinado:
            afinar = random.randint(0,1)
            if afinar == 1:
                esta_afinado = True
            else:
                print("No afinado")
                raise No_Afinado_Exception('El instrumento no está afinado')
        return "El instrumento esta afinado"

    @decorador_logs_tocar
    def tocar_instrumento(self):
        log.info("Tocamos el instrumento {}".format(self.nombre))


class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, num_cuerdas):
        super().__init__(nombre=nombre, tipo=tipo)
        self.num_cuerdas = num_cuerdas


class Guitarra_Electrica(Guitarra):
    def __init__(self, nombre, tipo, num_cuerdas, potencia):
        super().__init__(nombre=nombre,tipo=tipo,num_cuerdas=num_cuerdas)
        self.potencia = potencia


class Piano(Instrumento):
    def __init__(self, nombre, tipo, num_teclas):
        super().__init__(nombre=nombre, tipo=tipo)
        self.num_teclas = num_teclas


class Tambor(Instrumento):
    def __init__(self, nombre, tipo, tamanio):
        super().__init__(nombre=nombre, tipo=tipo)

    def aporrear(self):
        log.info("Aporreo como un makako")
