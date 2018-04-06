

import datetime
from Chequeo import chequeo

class persona(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None

    def __init__(self):
        self.lista_de_chequeos = []

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self,apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def setFecha_Nacimiento(self,fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def getFecha_Nacimiento(self):
        return self.fecha_nacimiento

    def AgregarChequeo(self,peso,altura,fecha):
        c = chequeo()
        c.setPeso(peso)
        c.setAltura(altura)
        c.setFecha(fecha)
        self.lista_de_chequeos.append(c)

    def BuscarChequeo(self,fecha):
        for item in self.lista_de_chequeos:
            if item.fecha == fecha:
                return item
        return None

    def PromedioPeso(self,año):
        prom_peso = 0
        fechas_de_chequeo = 0
        for item in self.lista_de_chequeos:
            if item.fecha.year == año:
                fechas_de_chequeo += 1
                prom_peso += item.peso
        return (prom_peso/fechas_de_chequeo)

    def PromedioAltura(self,año):
        prom_altura = 0
        fechas_de_chequeo = 0
        for item in self.lista_de_chequeos:
            if item.fecha.year == año:
                fechas_de_chequeo += 1
                prom_altura += item.altura
        return (prom_altura/fechas_de_chequeo)

    def PorcentajeCrecimiento(self,año1,año2):
        return ((self.PromedioAltura(año2) * 100) / self.PromedioAltura(año1)) - 100











