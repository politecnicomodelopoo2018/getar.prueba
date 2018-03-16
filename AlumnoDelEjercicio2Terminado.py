#unaM = una materia

import datetime
from MateriaDelEjercicio2Terminado import Materia

class alumno(object):
    nombre = None
    apellido = None
    fecha_de_nacimiento = None
    promedio = None

    def __init__(self):
        self.ListaMaterias = []

    def AgregarMateria(self,nombreMateria):
        unaM = Materia (nombreMateria)
        self.ListaMaterias.append(unaM)

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setFecha_de_nacimiento(self, fecha_de_nacimiento):
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def edad(self):
        fecha = datetime.date.today()
        dif = fecha - self.fecha_de_nacimiento
        dias = dif.days
        return dias/365.25

    def EncontrarMateria(self,nombreMateria):
        for item in self.ListaMaterias:
            if item.nombre == nombreMateria:
                return item
            return None

    def AgregarNotaAMateria(self,nombreMateria,nota):
        m = self.EncontrarMateria(nombreMateria)
        if m == None:
            return False
        m.AgregaNota(nota)
        return True

    def PromedioGeneral(self):
        if len(self.ListaMaterias) == 0:
            return False
        s = 0
        for item in self.ListaMaterias:
            s+= item.promedio()
        return s/len(self.ListaMaterias)

    def MenorNotaGeneral(self):
        listaAuxiliar = []
        for item in self.ListaMaterias:
            if item.menorNota() == None:
                listaAuxiliar.append(item.menorNota())
        return min(listaAuxiliar)

    def MayorNotaGeneral(self):
        listaAuxiliar2 = []
        for item in self.ListaMaterias:
            if item.mayorNota() == None:
                listaAuxiliar2.append(item.mayorNota())
        return max(listaAuxiliar2)

    def MenorPromedio(self):
        listaAuxiliar3 = []
        for item in self.ListaMaterias:
            if item.menorNota() == None:
                listaAuxiliar3.append(item.promedio())
        return min(listaAuxiliar3)

    def MayorPromedio(self):
        listaAuxiliar4 = []
        for item in self.ListaMaterias:
            if item.mayorNota() == None:
                listaAuxiliar4.append(item.promedio())
        return max(listaAuxiliar4)

















