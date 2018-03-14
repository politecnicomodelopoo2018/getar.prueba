import datetime

class alumno(object):
    nombre = None
    apellido = None
    fecha_de_nacimiento = None


    def __init__(self,notas):
        self.ListaNotas = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFecha_de_nacimiento(self, fecha_de_nacimiento):
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def AgregarNota (self, nota):
        if nota > 10:
            return False
        if nota < 1:
            return False
        self.ListaNotas.append(nota)
        return True

    def MayorNota (self):
        return max(self.ListaNotas)

    def MenorNota (self):
        return min(self.ListaNotas)

    def Promedio (self):
        if len(self.ListaNotas) == 0
            return False


    def edad (self):
        fecha = datetime.date.today()
        dif = fecha - self.fecha_de_nacimiento
        dias = dif.days
        return dias/365.25









