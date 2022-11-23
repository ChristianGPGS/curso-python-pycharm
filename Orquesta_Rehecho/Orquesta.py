import utils.logging_orquesta as log
from Clases import *


class Orquesta:
    def __init__(self, nombre):
        self._nombre = nombre
        self.lista_instrumentos = []

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self, nombre):
            self._nombre = nombre

    def crear_orquesta(self):
        log.info(f"Iniciando orquesta {self._nombre}")
        guitarra = Guitarra("Guitarra", "Española", 5)
        guitarra_electrica = Guitarra_Electrica("Guitarra", "Española", 5, 150)
        piano = Piano("Piano", "Clasico", 150)
        tambor = Tambor("Tambor1", "Tambor", "Grande")

        self.lista_instrumentos = [guitarra, guitarra_electrica, piano, tambor]

        def iniciar_concierto(self):
            log.info(f"Iniciando Concierto")
            self.afinar_instrumentos()
            self.tocar_instrumentos()

        def afinar_instrumentos(self):
            log.info(f"Afinando Instrumentos:")
            for instrumento in self.lista_instrumetos:
                instrumento.afinar()

        def tocar_instrumentos(self):
            log.info(f"Tocar Instrumentos:")
            try:
                for instrumento in self.lista_instrumetos:
                    if isinstance(instrumento, Tambor):
                        instrumento.aporrear()
                    else:
                        instrumento.tocar()
            except Instrumento_no_Afinado as ina:
                log.error(ina)
                log.info("El concierto se detiene porque un instrumento no está afinado")
                self.iniciar_concierto()

if __name__ == '__main__':
    log.info(f"Empezando")
    orquesta = Orquesta("Orquesta Mondragon")
    orquesta.crear_orquesta()
    orquesta.iniciar_concierto()