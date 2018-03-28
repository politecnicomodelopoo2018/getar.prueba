from equipo import Equipo

class campeonato(object):

    def __init__(self):
        self.ListaEquipos = []

    def AgregarEquipo (self,nombre_equipo,barrio):
        eq = Equipo()
        eq.nombre_equipo = nombre_equipo
        eq.barrio = barrio
        self.ListaEquipos



