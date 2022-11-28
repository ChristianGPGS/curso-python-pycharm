from Carrera_Caballos.DAO.Tabla_Gran_Premio import GranPremioDao
from Carrera_Caballos.DAO.Tabla_Apostantes import ApostantesDao
from Carrera_Caballos.DAO.Tabla_Caballos import CaballosDao

from utils.logging_carrera_caballos_main import log


def empezar_apuestas():
    granpremio_dao = GranPremioDao()
    apostante_dao = ApostantesDao()
    caballos_dao = CaballosDao()
    lista_gps = granpremio_dao.seleccionar()
    lista_apostantes = apostante_dao.seleccionar()
    lista_caballos = caballos_dao.seleccionar()
    caballo_a_apostar = ""
    for gp in lista_gps:
        for carrera in range(gp.num_carreras):
            log.debug("Bienvenidos a la carrera {}!!".format(carrera + 1))
            log.debug("La carrera tiene {} metros de distancia".format(gp.distancia))
            for apostante in lista_apostantes:
                log.debug("Usted es {} y tiene {} $".format(apostante.nombre, apostante.saldo))
                if apostante.saldo > 0:
                    dinero_apostar = int(input("Cuanto dinero quiere apostar?"))
                    if dinero_apostar > apostante.saldo or dinero_apostar < 0:
                        log.error("No tienes ese dinero.")
                    else:
                        saldo_actual = apostante.saldo - dinero_apostar
                        apostante.saldo = saldo_actual
                        apostante_dao.actualizar(apostante)
                        log.debug("saldo actual del apostante {} es:".format(apostante.nombre, apostante.saldo))
                        for caballos in lista_caballos:
                            log.info("{}-{}-{}".format(caballos.id, caballos.nombre, caballos.valor_apuesta))
                            caballo_a_apostar = int(input("Por que caballo quiere apostar?"))
                            if caballo_a_apostar > caballos.id or caballo_a_apostar < caballos.id:
                                log.error("Ese caballo no existe")
                        log.debug(caballo_a_apostar)


if __name__ == '__main__':
    empezar_apuestas()
