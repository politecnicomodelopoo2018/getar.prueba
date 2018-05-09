class Persona(object):
    nombre = None
    apellido = None
    DNI = None
    fecha_ingreso = None

    def __init__(self,nombre,apellido,DNI,fecha_ingreso):
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.fecha_ingreso = fecha_ingreso

