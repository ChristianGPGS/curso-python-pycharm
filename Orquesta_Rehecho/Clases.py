import utils.logging_orquesta as log
from abc import ABC, abstractmethod
from utils.general_utils import generar_aleatorio_booleano
from Excepciones import Instrumento_no_Afinado
from Decoradores import decorador_logs


class Instrumento(ABC):
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo
        self._afinado = False

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self, nombre):
            self._nombre = nombre

            @property
            def tipo(self):
                return self._tipo

            @tipo.setter
            def tipo(self, tipo):
                self._tipo = tipo

                @property
                def afinado(self):
                    return self._afinado

                @afinado.setter
                def afinado(self, afinado):
                    self._afinado = afinado

    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def tocar_instrumento(self):
        pass

    def limpiar(self):
        log.info("Limpiando instrumento")


class Guitarra(Instrumento):
    def __init__(self, nombre, tipo, num_cuerdas):
        Instrumento.__init__(self, nombre, tipo)
        self._num_cuerdas = num_cuerdas

        @property
        def num_cuerdas(self):
            return self._num_cuerdas

        @num_cuerdas.setter
        def num_cuerdas(self, num_cuerdas):
            self._num_cuerdas = num_cuerdas

        @decorador_logs
        def tocar(self):
            if self.afinado:
                log.info(f"Tocando la guitarra {self.nombre}")
            else:
                raise Instrumento_no_Afinado(f"La guitarra {self.nombre} no esta afinada correctamente")

        @decorador_logs
        def afinar(self):
            if generar_aleatorio_booleano(2):
                self.afinado = True
                log.info(f"Guitarra {self.nombre} afinada correctamente")
            else:
                self.afinado = False
                log.info(f"Guitarra {self.nombre} NO afinada correctamente")

        def limpiar(self):
            super().limpiar()
            print("Limpiando instrumento")


class Guitarra_Electrica(Guitarra):
    def __init__(self, nombre, tipo, num_cuerdas, potencia):
        super().__init__(nombre, tipo, num_cuerdas)
        self._potencia = potencia

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia

    @decorador_logs
    def tocar(self):
        super().tocar()
        log.info(f"Tocando Guitarra Electrica con {self.potencia} vatios de potencia")


class Piano(Instrumento):
    def __init__(self, nombre, tipo, num_teclas):
        super().__init__(nombre, tipo)
        self._num_teclas = num_teclas

    @property
    def num_teclas(self):
        return self._num_teclas

    @num_teclas.setter
    def num_teclas(self, num_teclas):
        self._num_teclas = num_teclas

    @decorador_logs
    def tocar(self):
        if self.afinado:
            log.info(f"Tocando Piano {self.nombre}")
        else:
            raise Instrumento_no_Afinado(f"La Piano {self.nombre} no esta afinada correctamente")

    @decorador_logs
    def afinar(self):
        if generar_aleatorio_booleano(2):
            self.afinado = True
            log.info(f"Piano {self.nombre} afinada correctamente")
        else:
            self.afinado = False
            log.info(f"Piano {self.nombre} NO afinada correctamente")


class Tambor(Instrumento):
    def __init__(self, nombre, tipo, tamanio):
        super().__init__(nombre, tipo)
        self._tamanio = tamanio

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def num_cuerdas(self, tamanio):
        self._tamanio = tamanio

    @decorador_logs
    def afinar(self):
        if generar_aleatorio_booleano(2):
            self.afinado = True
            log.info(f"Tambor {self.nombre} afinado correctamente")
        else:
            self.afinado = False
            log.info(f"Tambor {self.nombre} NO afinado correctamente")

    @decorador_logs
    def tocar(self):
        if self.afinado:
            log.info(f"Tocando Tambor {self.nombre} con un tamaño {self.tamanio}")
        else:
            raise Instrumento_no_Afinado(f"El tambor {self.nombre} no esta afinado correctamente")

    def aporrear(self):
        log.info(f"Aporreando Tambor {self.nombre} con un tamaño {self.tamanio}")
