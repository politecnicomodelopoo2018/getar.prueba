class Persona(object):
    nombre = None
    apellido = None

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Alumno(Persona):
    division = None

    def __init__(self,nombre,apellido,division):
        Persona.__init__(nombre,apellido)
        self.division = division

class Profesor(Persona):
    descuento = None

    def __init__(self,nombre,apellido,descuento):
        Persona.__init__(nombre,apellido)
        self.descuento = descuento