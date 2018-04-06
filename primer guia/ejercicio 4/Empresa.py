#listaE = lista de empleados
from Empleado import empleado

class empresa(object):
    nombre_empresa = None

    def __init__(self):
        self.listaE = []

    def setNombre(self,nombre_empresa):
        self.nombre_empresa = nombre_empresa

    def getNombre(self):
        return self.nombre_empresa

    def AñadirEmpleado(self,nombre_empleado,apellido_empleado,fecha_nacimiento,telefono):
        e = empleado()
        e.setNombre(nombre_empleado)
        e.setApellido(apellido_empleado)
        e.setFecha_nacimiento(fecha_nacimiento)
        e.setTelefono(telefono)
        self.listaE.append(e)

    def BuscarEmpleado(self,nombre_empleado):
        for item in self.listaE():
            if item.nombre_empleado == nombre_empleado:
                return item
            return None

    def porcDeAsist(self,año,mes):
        if len(self.listaE) == 0:
            return None
        suma = 0
        for item in self.listaE:
            suma += item.porcDeAsist(año,mes)
        return suma / len(self.listaE)



