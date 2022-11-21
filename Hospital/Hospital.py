import Hospital_clases as H
class Hospital:
    enfermedades = ["Gripe", "Brazo Roto", "Covid-19", "Dolor de cabeza"]

    paciente1 = H.Pacientes("Dolor de cabeza", "paciente1")
    paciente2 = H.Pacientes("Dolor de tripa", "paciente1")
    paciente3 = H.Pacientes("Le falta un brazo", "paciente1")
    paciente4 = H.Pacientes("Se ha dado un golpe", "paciente1")

    sala_espera = [paciente1, paciente2, paciente3, paciente4]

    doctor1 = H.Doctor("Doctor1", "Especialidad1")
    doctor2 = H.Doctor("Doctor2", "Especialidad2")
    consulta =  {doctor1: "", doctor2: ""}

    enfermero1 = H.Enfermero("enfermero1", 1)
    enfermero2 = H.Enfermero("enfermero2", 2)

    enfermeros = [enfermero1, enfermero2]

    habitaciones = []

    for enfermero in enfermeros:
        enfermero.fichar(enfermero.nombre)
        enfermero.atender_paciente(enfermeros, sala_espera, consulta, enfermedades, habitaciones)
