from persona import Alumno
from persona import Profesor
from plato import Plato
from pedido import Pedido

class Menu(object):

    def __init__(self):
        self.lista_alumnos = []
        self.lista_profesores = []
        self.lista_platos = []
        self.lista_pedidos = []

    def AgregarAlumno(self,A):
        A = Alumno()
        self.lista_alumnos.append(A)

    def AgregarProfesor(self,Pr):
        Pr = Profesor()
        self.lista_profesores.append(Pr)

    def AgregarPlato(self,Pl):
        Pl = Plato()
        self.lista_platos.append(Pl)

    def AgregarPedido(self,Pe):
        Pe = Pedido()
        self.lista_pedidos.append(Pe)

    def EliminarAlumno(self,nombre,apellido):
        for item in self.lista_alumnos:
            if item.nombre == nombre and item.apellido == apellido:
                self.lista_alumnos.remove(item)

    def EliminarProfesor(self,nombre,apellido):
        for item in self.lista_profesores:
            if item.nombre == nombre and item.apellido == apellido:
                self.lista_profesores.remove(item)

    def EliminarPlato(self,nombre_plato):
        for item in self.lista_platos:
            if item.nombre_plato == nombre_plato:
                self.lista_platos.remove(item)

    def EliminarPedido(self,pe,pl):
        for item in self.lista_pedidos:
            if item.persona == pe and item.plato == pl:
                self.lista_pedidos.remove(item)

    def ModificarAlumno(self,A,nuevo_nombre,nuevo_apellido,nueva_division):
        A = Alumno
        A.nombre = nuevo_nombre
        A.apellido = nuevo_apellido
        A.division = nueva_division

    def ModificarProfesor(self,Pr,nuevo_nombre,nuevo_apellido,nuevo_descuento):
        Pr = Profesor
        Pr.nombre = nuevo_nombre
        Pr.apellido = nuevo_apellido
        Pr.descuento = nuevo_descuento

    def ModificarPlato(self,Pl,nuevo_nombre_plato,nuevo_precio):
        Pl = Plato()
        Pl.nombre_plato = nuevo_nombre_plato
        Pl.precio = nuevo_precio
