# -*- coding: utf-8 -*-


# 1

class alumno (object):
    nombre = None
    apellido = None
    fecha_de_nacimiento = None


    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def __init__(self,notas):
        self.ListaNotas = []


a = alumno()
n= imput("Ingresa tu nombre")
a.setNombre(n)
print(a.getNombre())

