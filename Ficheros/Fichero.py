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

#Constantes
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

    #reemplazar este for por el de abajo y descomentar las cuentas de arriba
    for linea_cortada in cortadas:
        if linea_cortada[0] == "Colegio1":
            # sube la cuenta del colegio para despues usar ese numero en la variable que crea los objetos
            cuenta_colegio1 += 1
            # le pongo formato para ponerlo como nombre en la variable que crea el objeto
            colegio1 = "Colegio{}".format(cuenta_colegio1)
            # creo el objeto usando los indices de la lista
            colegio1 = Colegio(linea_cortada[COLEGIO], linea_cortada[NOMBRE_ALUMNO], linea_cortada[APELLIDO_ALUMNO], linea_cortada[DNI], linea_cortada[ASIGNATURAS].split(SEPARADOR_ASIGNATURAS))
            # creo el archivo con los datos del objeto
            archivo_escritura1.write(str(colegio1.imprimir()))
        elif linea_cortada[0] == "Colegio2":
            # sube la cuenta del colegio para despues usar ese numero en la variable que crea los objetos
            cuenta_colegio2 += 1
            # le pongo formato para ponerlo como nombre en la variable que crea el objeto
            colegio2 = "Colegio{}".format(cuenta_colegio2)
            # creo el objeto usando los indices de la lista
            colegio2 = Colegio(linea_cortada[COLEGIO], linea_cortada[NOMBRE_ALUMNO], linea_cortada[APELLIDO_ALUMNO], linea_cortada[DNI], linea_cortada[ASIGNATURAS].split(SEPARADOR_ASIGNATURAS))
            # creo el archivo con los datos del objeto
            archivo_escritura2.write(str(colegio2.imprimir()))
        elif linea_cortada[0] == "Colegio3":
            # sube la cuenta del colegio para despues usar ese numero en la variable que crea los objetos
            cuenta_colegio3 += 1
            # le pongo formato para ponerlo como nombre en la variable que crea el objeto
            colegio3 = "Colegio{}".format(cuenta_colegio3)
            # creo el objeto usando los indices de la lista
            colegio3 = Colegio(linea_cortada[COLEGIO], linea_cortada[NOMBRE_ALUMNO], linea_cortada[APELLIDO_ALUMNO], linea_cortada[DNI], linea_cortada[ASIGNATURAS].split(SEPARADOR_ASIGNATURAS))
            # creo el archivo con los datos del objeto
            archivo_escritura3.write(str(colegio3.imprimir()))
    log.info("Archivos creados con exito")

    archivo_escritura1.close()
    archivo_escritura2.close()
    archivo_escritura3.close()

except Exception as e:
    print(e)
finally:
    archivo.close()

    """
        for linea_cortada in cortadas:
    # print(linea_cortada)
    if linea_cortada[0] == "Colegio1":
        if linea_cortada[-1].count(";") > 0:
            linea_cortada.append(linea_cortada[-1].split(";"))
            colegios1.append(linea_cortada)
    elif linea_cortada[0] == "Colegio2":
        if linea_cortada[-1].count(";") > 0:
            test = linea_cortada[-1].split(";")
            linea_cortada.append(test[0])
            linea_cortada.append(test[1])
            colegios2.append(linea_cortada)
    elif linea_cortada[0] == "Colegio3":
        if linea_cortada[-1].count(";") > 0:
            linea_cortada.append(linea_cortada[-1].split(";"))
            colegios3.append(linea_cortada)
    """
