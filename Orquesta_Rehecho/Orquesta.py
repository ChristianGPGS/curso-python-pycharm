import utils.logging_orquesta as log
import Clases as c
from Excepciones import no_afinar_exception

class Orquesta:

    def crear_orquesta():

        guitarra = c.Guitarra("guitarra1","Guitarra",5)
        guitarra_electrica = c.Guitarra_Electrica("Guitarra_Electrica","Guitarra_Electrica",5,100)
        piano = c.Piano("piano","piano",88)
        tambor = c.Tambor("tambor","tambor","grande")
        lista_instrumetos = [guitarra,guitarra_electrica,piano,tambor]

        return lista_instrumetos
    def iniciar_concierto(lista_instrumetos):
        for instrumento in lista_instrumetos:
            log.debug("El nombre del intrumento es {}".format(instrumento.nombre))
            try:
                instrumento.afinar()
                if instrumento.tipo == "tambor":
                    instrumento.aporrear()
                else:
                    instrumento.tocar_instrumento()
            except no_afinar_exception as a:
                log.error(a.mensaje)
            except Exception as e:
                log.error(f'Exception - Ocurrió un error: {e} , {type(e)}')


    lista_instrumetos = crear_orquesta()
    iniciar_concierto(lista_instrumetos)
