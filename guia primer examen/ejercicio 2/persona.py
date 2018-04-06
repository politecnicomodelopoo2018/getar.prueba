from plato import Plato

class Persona(object):
    class persona(object):
        nombre = None
        fecha_nacimiento = None

        def __init__(self):
            self.platos = []

        def setNombre(self, nombre):
            self.nombre = nombre

        def getNombre(self):
            return self.nombre

        def setFecha_Nacimiento(self, fecha_nacimiento):
            self.fecha_nacimiento = fecha_nacimiento

        def getFecha_Nacimiento(self):
            return self.fecha_nacimiento

        def Comer(self):
            P = Plato()
            self.platos.append(P)

        def SumaCalorias(self):
            sumador_calorias = 0
            for item in self.platos:
                sumador_calorias += item.calorias
            return sumador_calorias


