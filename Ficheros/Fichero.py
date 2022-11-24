import utils.logging_colegio as log


class Colegio:
    def __init__(self, colegio, nombre, apellido, dni, asignatura):
        self.colegio = colegio
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.asignatura = asignatura

    def imprimir(self):
        return self.colegio, self.nombre, self.apellido, self.dni, self.asignatura


# Constantes
COLEGIO = 0
NOMBRE_ALUMNO = 1
APELLIDO_ALUMNO = 2
DNI = 3
ASIGNATURAS = 4
SEPARADOR_ASIGNATURAS = ";"

try:
    archivo = open('alumnos-colegio.txt', 'r', encoding='utf8')
    archivo_escritura1 = open('colegio1.txt', 'w', encoding='utf8')
    archivo_escritura2 = open('colegio2.txt', 'w', encoding='utf8')
    archivo_escritura3 = open('colegio3.txt', 'w', encoding='utf8')

    cuenta_colegio1 = 0
    cuenta_colegio2 = 0
    cuenta_colegio3 = 0

    colegios1 = []
    colegios2 = []
    colegios3 = []

    cortadas = []
    for linea in archivo:
        cortadas.append(linea.split("|"))
    archivo.close()

    for linea_cortada in cortadas:
        if linea_cortada[0] == "Colegio1":
            cuenta_colegio1 += 1
            colegio1 = "Colegio{}".format(cuenta_colegio1)
            colegio1 = Colegio(linea_cortada[COLEGIO], linea_cortada[NOMBRE_ALUMNO], linea_cortada[APELLIDO_ALUMNO],
                               linea_cortada[DNI], linea_cortada[ASIGNATURAS].split(SEPARADOR_ASIGNATURAS))
            archivo_escritura1.write(str(colegio1.imprimir()))
        elif linea_cortada[0] == "Colegio2":
            cuenta_colegio2 += 1
            colegio2 = "Colegio{}".format(cuenta_colegio2)
            colegio2 = Colegio(linea_cortada[COLEGIO], linea_cortada[NOMBRE_ALUMNO], linea_cortada[APELLIDO_ALUMNO],
                               linea_cortada[DNI], linea_cortada[ASIGNATURAS].split(SEPARADOR_ASIGNATURAS))
            archivo_escritura2.write(str(colegio2.imprimir()))
        elif linea_cortada[0] == "Colegio3":
            cuenta_colegio3 += 1
            colegio3 = "Colegio{}".format(cuenta_colegio3)
            colegio3 = Colegio(linea_cortada[COLEGIO], linea_cortada[NOMBRE_ALUMNO], linea_cortada[APELLIDO_ALUMNO],
                               linea_cortada[DNI], linea_cortada[ASIGNATURAS].split(SEPARADOR_ASIGNATURAS))
            archivo_escritura3.write(str(colegio3.imprimir()))
    log.info("Archivos creados con exito")

    archivo_escritura1.close()
    archivo_escritura2.close()
    archivo_escritura3.close()

except Exception as e:
    print(e)
finally:
    archivo.close()