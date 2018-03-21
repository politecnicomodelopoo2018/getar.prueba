from Empleado import empleado

class empresa(object):
    nombre_empresa = None

    def __init__(self):
        lista_empleados = []

    def setNombre(self,nombre_empresa):
        self.nombre_empresa = nombre_empresa

    def getNombre(self):
        return self.nombre_empresa


