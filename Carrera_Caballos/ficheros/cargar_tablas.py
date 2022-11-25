from datetime import datetime

from Carrera_Caballos.DAO.Tabla_Apostantes import ApostantesDao
from Carrera_Caballos.DAO.Tabla_Caballos import CaballosDao
from Carrera_Caballos.DAO.Tabla_Gran_Premio import GranPremioDao
from Carrera_Caballos.POJO.Caballos import Caballos
from Carrera_Caballos.POJO.Apostantes import Apostantes
from Carrera_Caballos.POJO.Gran_Premio import GranPremio
from utils.logging_carrera_caballos import log

SEPARADOR = "|"
# Apostantes
NOMBRE_APOSTANTE = 0
SALDO = 1

# Gran_Premio
NOMBRE_GRAN_PREMIO = 0
DISTANCIA = 1
NUM_CARRERAS = 2

# Caballos
NOMBRE_CABALLO = 0
FECHA_NACIMIENTO = 1
VELOCIDAD = 2
EXPERIENCIA = 3
VALOR_APUESTA = 4
ID_GRAN_PREMIO = 5

if __name__ == '__main__':
    log.debug("Empezamos a leer el archivo 'Apostantes.txt'")
    with open('Apostantes.txt', 'r', encoding='utf8') as apostantes:
        for linea in apostantes:
            datos = linea.split(SEPARADOR)
            apostante = Apostantes(datos[NOMBRE_APOSTANTE], datos[SALDO])
            apostanteDAO = ApostantesDao()
            apostanteDAO.insertar(apostante)

    log.debug("Empezamos a leer el archivo 'Gran_Premio.txt'")
    with open('grandes_premios.txt', 'r', encoding='utf8') as gran_premio:
        for linea in gran_premio:
            datos = linea.split(SEPARADOR)
            gran_premio = GranPremio(datos[NOMBRE_GRAN_PREMIO], datos[DISTANCIA], datos[NUM_CARRERAS])
            granpremioDAO = GranPremioDao()
            granpremioDAO.insertar(gran_premio)

    log.debug("Empezamos a leer el archivo 'Caballos.txt'")
    with open('Caballos.txt', 'r', encoding='utf8') as caballos:
        for linea in caballos:
            datos = linea.split(SEPARADOR)
            caballo = Caballos(datos[NOMBRE_CABALLO], datos[FECHA_NACIMIENTO], datos[VELOCIDAD], datos[EXPERIENCIA],
                               datos[VALOR_APUESTA], datos[ID_GRAN_PREMIO])
            caballoDAO = CaballosDao()
            caballoDAO.insertar(caballo)