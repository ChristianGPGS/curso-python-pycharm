import random
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre


class Profesional():
    def fichar(self, nombre):
        print("{} ha fichado".format(nombre))


class Doctor(Persona, Profesional):
    def __init__(self, nombre, especialidad):
        Persona.__init__(self, nombre)
        self.especialidad = especialidad

    def diagnosticar(self, enfermo, enfermedades, habitaciones, consulta):
        if random.randint(1, 10) >= 7:
            enfermedad = enfermedades[random.randint(0, len(enfermedades)-1)]
            print("Usted tiene: {}".format(enfermedad))
            enfermo = Enfermos( enfermedad,enfermo.nombre)
            habitaciones.append(enfermo.nombre)
            return consulta.keys()
        else:
            print("Usted no está enfermo")


class Enfermero(Persona, Profesional):
    def __init__(self, nombre, planta):
        self.planta = planta
        Persona.__init__(self, nombre)

    def atender_paciente(self, enfermero, sala_espera, consulta, enfermedades, habitaciones):
        hay_enfermos = True

        while hay_enfermos:
            hay_enfermos = len(sala_espera) != 0
            for enfermo in sala_espera:
                if hay_enfermos:
                    print("Se le hace pasar a una consulta")
                    for doctor in consulta:
                        doctor.fichar(doctor.nombre)
                        doctor.diagnosticar(enfermo, enfermedades, habitaciones, consulta)
                        sala_espera.pop(0)
        for habitacion in habitaciones:
            print("Habitaciones: {}".format(str(habitacion)))



class Pacientes(Persona):
    def __init__(self, sintomas, nombre):
        self.sintomas = sintomas
        Persona.__init__(self, nombre)


class Enfermos(Persona):
    def __init__(self, enfermedad, nombre):
        self.enfermedad = enfermedad
        Persona.__init__(self, nombre)