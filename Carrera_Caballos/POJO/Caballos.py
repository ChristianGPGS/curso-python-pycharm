class Caballos:
    def __init__(self, nombre=None, fecha_nacimiento=None, velocidad=None, experiencia=None,
                 valor_apuesta=None, id_gran_premio=None, id=None):
        self._id = id
        self._nombre = nombre
        self._fecha_nacimiento = fecha_nacimiento
        self._velocidad = velocidad
        self._experiencia = experiencia
        self._valor_apuesta = valor_apuesta
        self._id_gran_premio = id_gran_premio
        self._distancia_recorrida = 0

    def __str__(self):
        return

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia

    @property
    def valor_apuesta(self):
        return self._valor_apuesta

    @valor_apuesta.setter
    def valor_apuesta(self, valor_apuesta):
        self._valor_apuesta = valor_apuesta

    @property
    def id_gran_premio(self):
        return self._id_gran_premio

    @id_gran_premio.setter
    def id_gran_premio(self, id_gran_premio):
        self._id_gran_premio = id_gran_premio

    @property
    def distancia_recorrida(self):
        return self._distancia_recorrida

    @distancia_recorrida.setter
    def distancia_recorrida(self, distancia_recorrida):
        self._distancia_recorrida = distancia_recorrida
