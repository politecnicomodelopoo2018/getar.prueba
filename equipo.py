from jugador import Jugador

class Equipo(object):
    nombre_equipo = None
    barrio = None

    def __init__(self,nombre_equipo = None,barrio = None):
        self.nombre_equipo = nombre_equipo
        self.barrio = barrio
        self.ListaJugadores = []
        self.ListaDiasQueJuega = []
        self.ListaHoraDelDia = []


    def AgregarJugadorAlEquipo(self, Jugador):
        if Jugador.capitan == True:
            for item in self.ListaJugadores:
                if item.capitan == True:
                    return 0
        self.ListaJugadores.append(Jugador)


