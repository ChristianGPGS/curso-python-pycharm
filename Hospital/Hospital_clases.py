import random


class Persona():
    def __init__(self, nombre):
        self.nombre = nombre


class Profesional():
    def fichar(self):
        pass


class Doctor(Persona, Profesional):
    def __init__(self, nombre, especialidad):
        Persona.__init__(self, nombre)
        self.especialidad = especialidad

    def diagnosticar(self, enfermo, enfermedades, habitaciones, consulta):
        print("Metodo Diagnosticar")
        if random.randint(1, 10) >= 7:
            enfermedad = random.randomchoice(enfermedades)
            print("Usted tiene: {}".format(enfermedad))
            enfermo = Enfermos(enfermo.nombre, enfermedad)
            habitaciones.append(enfermo)
            return consulta.get(consulta.key)
        else:
            print("Usted no está enfermo")
            paciente_consulta = consulta.get(consulta.key)
            print(consulta.remove(consulta.value(paciente_consulta)))


class Enfermero(Persona, Profesional):
    def __init__(self, nombre, planta):
        self.planta = planta
        Persona.__init__(self, nombre)

    def atender_paciente(self, enfermero, sala_espera, consulta, enfermedades, habitaciones):
        print("Metodo atender_paciente")
        hay_enfermos = len(sala_espera) > 0

        while hay_enfermos:
            for enfermo in sala_espera:
                if hay_enfermos:
                    print("Se le hace pasar a una consulta")
                    for doctor in consulta:
                        doctor.diagnosticar(enfermo, enfermedades, habitaciones)
                else:
                    sala_espera.pop(enfermo)
            enfermero.fichar()


class Pacientes(Persona):
    def __init__(self, sintomas, nombre):
        self.sintomas = sintomas
        Persona.__init__(self, nombre)


class Enfermos(Persona):
    def __init__(self, enfermedad, nombre):
        self.enfermedad = enfermedad
        Persona.__init__(self, nombre)
