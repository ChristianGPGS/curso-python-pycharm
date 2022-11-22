# Incluye todas las clases relacionadas con las personas
import utils.logging_bar as log
import Taza_cafe as tc
import random
from abc import ABC
from temperature_exception import toocold_exception, toohot_exception


class Persona(ABC):
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class Cliente(Persona):

    def tomar_taza_cafe(self, temperatura):
        if temperatura >= 80:
            raise toohot_exception('El cafe está muy caliente, su temperatura es de {}'.format(temperatura))
        elif temperatura <= 20:
            raise toocold_exception('El cafe esta demasiado frio, su temperatura es de {}'.format(temperatura))
        else:
            log.info("El cafe esta perfecto, su temperatura es de {}".format(temperatura))


class Camarero(Persona):

    def servir_taza_cafe(self):
        tipos_de_cafe = ["tipo1", "tipo2", "tipo3", "tipo4"]

        tipo_cafe = input("Buenas tardes, que tipo de cafe quiere? {}".format(tipos_de_cafe))
        if tipo_cafe not in tipos_de_cafe:
            self.servir_taza_cafe()
        else:
            taza_cafe = tc.Taza_cafe(random.randint(0, 100), tipo_cafe)
            return taza_cafe
