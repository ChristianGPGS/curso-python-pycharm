# Guardar en objetos
# Generar archivos con el nombre del colegio con los datos de los alumnos de cada colegio
class Colegio:
    def __init__(self, colegio, nombre, apellido, dni, asignatura):
        self.colegio = colegio
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.asignatura = asignatura

    def imprimir(self):
        return self.colegio, self.nombre, self.apellido, self.dni, self.asignatura


try:
    archivo = open('alumnos-colegio.txt', 'r', encoding='utf8')
    archivo_escritura1 = open('colegio1.txt', 'w', encoding='utf8')
    archivo_escritura2 = open('colegio2.txt', 'w', encoding='utf8')
    archivo_escritura3 = open('colegio3.txt', 'w', encoding='utf8')

    # cuenta_colegio1 = 0
    # cuenta_colegio2 = 0
    # cuenta_colegio3 = 0

    colegios1 = []
    colegios2 = []
    colegios3 = []

    cortadas = []
    for linea in archivo:
        cortadas.append(linea.split("|"))
    archivo.close()

    for linea_cortada in cortadas:
        # print(linea_cortada)
        if linea_cortada[0] == "Colegio1":
            if linea_cortada[-1].count(";") > 0:
                # hacer un split?
                colegios1.append(linea_cortada)
        elif linea_cortada[0] == "Colegio2":
            colegios2.append(linea_cortada)
        elif linea_cortada[0] == "Colegio3":
            colegios3.append(linea_cortada)

    print(colegios1)
    print(colegios2)
    print(colegios3)

    print("Archivos creados con exito")

    archivo_escritura1.close()
    archivo_escritura2.close()
    archivo_escritura3.close()

except Exception as e:
    print(e)
finally:
    archivo.close()

    """
        for linea_cortada in cortadas:
        if linea_cortada[0] == "Colegio1":
            #sube la cuenta del colegio para despues usar ese numero en la variable que crea los objetos
            cuenta_colegio1 += 1
            #le pongo formato para ponerlo como nombre en la variable que crea el objeto
            colegio1 = "Colegio{}".format(cuenta_colegio1)
            #creo el objeto usando los indices de la lista
            colegio1 = Colegio(linea_cortada[0], linea_cortada[1], linea_cortada[2], linea_cortada[3], linea_cortada[4])
            #creo el archivo con los datos del objeto
            archivo_escritura1.write(str(colegio1.imprimir()))
        elif linea_cortada[0] == "Colegio2":
            #sube la cuenta del colegio para despues usar ese numero en la variable que crea los objetos
            cuenta_colegio2 += 1
            #le pongo formato para ponerlo como nombre en la variable que crea el objeto
            colegio2 = "Colegio{}".format(cuenta_colegio2)
            #creo el objeto usando los indices de la lista
            colegio2 = Colegio(linea_cortada[0], linea_cortada[1], linea_cortada[2], linea_cortada[3], linea_cortada[4])
            #creo el archivo con los datos del objeto
            archivo_escritura2.write(str(colegio2.imprimir()))
        elif linea_cortada[0] == "Colegio3":
            #sube la cuenta del colegio para despues usar ese numero en la variable que crea los objetos
            cuenta_colegio3 += 1
            #le pongo formato para ponerlo como nombre en la variable que crea el objeto
            colegio3 = "Colegio{}".format(cuenta_colegio3)
            #creo el objeto usando los indices de la lista
            colegio3 = Colegio(linea_cortada[0], linea_cortada[1], linea_cortada[2], linea_cortada[3], linea_cortada[4])
            #creo el archivo con los datos del objeto
            archivo_escritura3.write(str(colegio3.imprimir()))
    print("Archivos creados con exito")

    archivo_escritura1.close()
    archivo_escritura2.close()
    archivo_escritura3.close()
    """
