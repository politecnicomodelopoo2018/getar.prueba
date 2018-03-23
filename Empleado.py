#ListaDias = lista de dias que tiene que presentarse a trabajar el empleado
#ListaAsistencias = lista de dias que el empleado se presenta a trabajar
#porcDeAsist = porcentaje de asistencias
#cDiasQueFue = cantidad de dias que el empleado fue a trabajar
#cDiasQueTieneQueIr = cantidad dedias que el empleado tiene que ir a trabajar

import datetime
import calendar


class empleado (object):
    nombre_empleado = None
    apellido_empleado = None
    fecha_nacimiento = None
    telefono = None

    def __init__(self):
        self.ListaAsistencias = []
        self.ListaDias = []

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

    def setlistaDias(self,ListaDias):
        self.ListaDias = ListaDias

    def AgregarAsistencia(self,fecha):
        self.ListaAsistencias.append(fecha)

    def porcDeAsist(self, año, mes):
        cDiasQueFue = 0
        cDiasQueTieneQueIr = 0
        cantDiasdelMes = calendar.monthrange(año,mes)[1]
        for i in range (1,cantDiasdelMes + 1):
            fecha = datetime.date(año,mes,i)
            if self.ListaDias[fecha.weekday()]:
                for item in self.ListaAsistencias:
                    if fecha == item:
                        cDiasQueFue += 1
                        break
                cDiasQueTieneQueIr += 1
        return cDiasQueFue / cDiasQueTieneQueIr








