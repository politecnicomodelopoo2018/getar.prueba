class Jugador(object):
    nombre_jugador = None
    fecha_nacimiento = None
    numero_camiseta = None
    capitan = False

    def setNombreJugador(self,nombre_jugador):
        self.nombre_jugador = nombre_jugador

    def setFechaNacimiento(self,fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def setNumeroCamiseta(self,numero_camiseta):
        self.numero_camiseta = numero_camiseta

    def setCapitan(self, estado):
        self.capitan = estado

