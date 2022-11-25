from Carrera_Caballos.POJO.Gran_Premio import GranPremio
from utils.conexiones import get_mysql_conection
from utils.logging_carrera_caballos import log


class GranPremioDao:
    _SELECCIONAR = 'SELECT * FROM gran_premio ORDER BY ID'
    _INSERTAR = 'INSERT INTO gran_premio(Nombre, Distancia, Num_Carreras) VALUES(%s, %s,%s)'
    _ACTUALIZAR = 'UPDATE gran_premio SET Nombre=%s, Distancia=%s, Num_Carreras=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM gran_premio WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                lista_gran_premio = []
                for registro in registros:
                    gran_premio = GranPremio(registro[1], registro[2], registro[3], registro[0])
                    lista_gran_premio.append(gran_premio)

                return lista_gran_premio

    @classmethod
    def insertar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (gran_premio.nombre, gran_premio.distancia, gran_premio.num_carreras)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'gran_premio insertado: {gran_premio.nombre}')
                conexion.commit()
                return cursor.rowcount

    @classmethod
    def actualizar(cls, gran_premio):
        with get_mysql_conection() as conexion:
            with conexion.cursor() as cursor:
                valores = (
                    gran_premio.id, gran_premio.nombre,  gran_premio.distancia,
                    gran_premio.num_carreras)
                cursor.execute(cls._ACTUALIZAR, valores)
                conexion.commit()
                log.debug(f'gran_premio actualizado: {gran_premio}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, gran_premio):
        with get_mysql_conection as conexion:
            with conexion.cursor as cursor:
                cursor.execute(cls._ELIMINAR, gran_premio.ID)
                conexion.commit()
                log.debug(f'Objeto eliminado: {gran_premio}')
                return cursor.rowcount
