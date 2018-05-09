from persona import Persona
from horario import Horario

class Programa(object):
    nombre = None
    operario = None
    categoria = None

    def __init__(self,nombre,categoria):
        self.nombre = nombre
        self.categoria = categoria
        self.lista_horarios = []
        self.lista_conductores = []

    def AgregarConductor(self,nombre,apellido,DNI,fecha_ingreso):
        P = Persona()
        P.nombre = nombre
        P.apellido = apellido
        P.DNI = DNI
        P.fecha_ingreso = fecha_ingreso
        self.lista_conductores.append(P)

    def SetOperario(self,nombre,apellido,DNI,fecha_ingreso):
        Pe = Persona()
        Pe.nombre = nombre
        Pe.apellido = apellido
        Pe.DNI = DNI
        Pe.fecha_ingreso = fecha_ingreso
        self.operario = Pe

    def AgregarHorario(self,dia,hora):
        H = Horario()
        H.dia = dia
        H.hora = hora
        self.lista_horarios.append(H)


