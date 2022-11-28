from utils.conexiones import get_mysql_conection
from Carrera_Caballos.POJO.Caballos import Caballos
from utils.logging_carrera_caballos import log


class CaballosDao:
    _SELECCIONAR = 'SELECT * FROM caballos ORDER BY ID'
    _INSERTAR = 'INSERT INTO caballos(Nombre, Fecha_nacimiento, Velocidad, Experiencia, Valor_apuesta, ' \
                'ID_gran_premio) VALUES(%s, %s, %s,%s, %s, %s) '
    _ACTUALIZAR = 'UPDATE caballos SET Nombre=%s, Fecha_nacimiento=%s, Velocidad=%s, Experiencia=%s, ' \
                  'Valor_apuesta=%s, ID_gran_premio=%s WHERE id=%s '
    _ELIMINAR = 'DELETE FROM caballos WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                lista_caballos = []
                for registro in registros:
                    caballos = Caballos(registro[1], registro[2], registro[3], registro[4], registro[5], registro[6],
                                        registro[0])
                    lista_caballos.append(caballos)

                return lista_caballos

    @classmethod
    def insertar(cls, caballos):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (caballos.nombre, caballos.fecha_nacimiento, caballos.velocidad, caballos.experiencia,
                           caballos.valor_apuesta, caballos.id_gran_premio)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'caballo insertado: {caballos.nombre}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def actualizar(cls, caballos):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (
                    caballos.id, caballos.nombre, caballos.fecha_nacimiento, caballos.felocidad, caballos.experiencia,
                    caballos.valor_apuesta, caballos.id_gran_premio)
                cursor.execute(cls._ACTUALIZAR, valores)
                conexion.commit()
                log.debug(f'caballo actualizada: {caballos}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, caballos):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, caballos.id)
                conexion.commit()
                log.debug(f'Objeto eliminado: {caballos}')
                return cursor.rowcount
