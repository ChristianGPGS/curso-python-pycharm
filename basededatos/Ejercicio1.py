"""
+ sacar toda la información de las personas que tengas un email *gmail.com

+ actualizais a las personas que no tengan un email de gmail con el dominio gmail.com
sadad@correo.es sadad@gmail.com

"""
from utils.conexiones import get_mysql_conection

"""
CREA LOS REGISTROS
try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO personas(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('persona1', 'apellido1', 'email1@gmail.com'),
                ('persona2', 'apellido2', 'email2@hotmail.com'),
                ('persona3', 'apellido3', 'email3@yahoo.com')
            )
            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')"""

# IMPRIME LOS NOMBRES
tabla = "personas"
try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = f'SELECT Nombre FROM {tabla}'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print("Los nombres de las personas son: ", registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')

# Hace el print pero con un filtro
try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = f'SELECT email FROM {tabla} WHERE email  like "%gmail.com"'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print("Los correos que contienen @gmail son: ", registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')


print(registros[0])
# Hace el update
"""
try:
    conexion = get_mysql_conection()
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE personas SET email = %s  not like "%gmail.com"'
            valores = f'{usernames}@gmail.com'
            cursor.execute(sentencia, valores)
            conexion.commit()
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
"""