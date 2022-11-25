from Carrera_Caballos.DAO.Tabla_Gran_Premio import GranPremioDao
from Carrera_Caballos.DAO.Tabla_Apostantes import ApostantesDao
from Carrera_Caballos.DAO.Tabla_Caballos import CaballosDao

from utils.logging_carrera_caballos_main import log


def empezar_carrera():
    granpremio_dao = GranPremioDao()
    apostante_dao = ApostantesDao()
    caballos_dao = CaballosDao()
    lista_gps = granpremio_dao.seleccionar()
    lista_apostantes = apostante_dao.seleccionar()
    lista_caballos = caballos_dao.seleccionar()

    for gp in lista_gps:
        for carrera in range(gp.num_carreras):
            log.debug(carrera+1)

if __name__ == '__main__':
    empezar_carrera()
