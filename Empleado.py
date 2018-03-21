import datetime

class empleado (object):
    nombre_empleado = None
    apellido_empleado = None
    fecha_nacimiento = None
    telefono = None

    def __init__(self):
        Dias_que_tiene_que_asistir = []

    def __init__(self):
        Dias_asistencia = []

    def setNombre(self, nombre_empleado):
        self.nombre_empleado = nombre_empleado

    def getNombre(self):
        return self.nombre_empleado

    def setApellido(self, apellido_empleado):
        self.apellido_empleado = apellido_empleado

    def getApellido(self):
        return self.apellido_empleado

    def setFecha_nacimiento(self,fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def getFecha_nacimiento(self):
        return self.fecha_nacimiento

    def setTelefono(self,telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono



