class Persona(object):
    nombre = None
    apellido = None

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def Descuento(self):
        return 0

class Alumno(Persona):
    division = None

    def __init__(self,nombre,apellido,division):
        Persona.__init__(self,nombre,apellido)
        self.division = division

class Profesor(Persona):
    descuento = None

    def Descuento(self):
        return self.descuento