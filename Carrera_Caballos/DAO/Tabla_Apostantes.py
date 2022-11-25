from utils.conexiones import get_mysql_conection
from Carrera_Caballos.POJO.Apostantes import Apostantes
from utils.logging_carrera_caballos import log


class ApostantesDao:
    _SELECCIONAR = 'SELECT * FROM apostantes ORDER BY ID'
    _INSERTAR = 'INSERT INTO apostantes(Nombre, Saldo) VALUES(%s, %s) '
    _ACTUALIZAR = 'UPDATE apostantes SET Nombre=%s, Saldo=%sWHERE id=%s '
    _ELIMINAR = 'DELETE FROM apostantes WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                lista_apostantes = []
                for registro in registros:
                    apostantes = Apostantes(registro[1], registro[2], registro[0])
                    lista_apostantes.append(apostantes)
                # de momento solo lo imprime, cambiar la lista para que devuelva los objetos
                return lista_apostantes

    @classmethod
    def insertar(cls, apostantes):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (apostantes.nombre, apostantes.saldo)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'apostante insertado: {apostantes.nombre}')
                conexion.commit()
                return cursor.rowcount

    """
                def insertar(cls, apostantes):
            conexion = get_mysql_conection()
            cursor = conexion.cursor()
            valores = (apostantes.nombre, apostantes.saldo)
            cursor.execute(cls._INSERTAR, valores)
            conexion.commit()
            log.debug(f'apostante insertado: {apostantes.nombre}')
            return cursor.rowcount
                """

    @classmethod
    def actualizar(cls, apostantes):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (
                    apostantes.ID, apostantes.Nombre, apostantes.Saldo)
                cursor.execute(cls._ACTUALIZAR, valores)
                conexion.commit()
                log.debug(f'apostante actualizada: {apostantes}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, apostantes):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._ELIMINAR, apostantes.ID)
                conexion.commit()
                log.debug(f'Objeto eliminado: {apostantes}')
                return cursor.rowcount
