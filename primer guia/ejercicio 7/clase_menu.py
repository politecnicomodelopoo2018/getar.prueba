from persona import Alumno
from persona import Profesor
from plato import Plato

class Menu(object):

    def __init__(self):
        self.lista_alumnos = []
        self.lista_profesores = []
        self.lista_platos = []
        self.lista_pedidos = []

    def AgregarAlumno(self,A):
        self.lista_alumnos.append(A)

    def AgregarProfesor(self,Pr):
        self.lista_profesores.append(Pr)

    def AgregarPlato(self,Pl):
        self.lista_platos.append(Pl)

    def AgregarPedido(self,Pe):
        self.lista_pedidos.append(Pe)

    def EliminarAlumno(self, nombre, apellido):
        a = None
        for item in self.lista_alumnos:
            if item.nombre == nombre and item.apellido == apellido:
                a = item
                break
        if not a:
            return False

        for item in self.lista_pedidos:
            if item.persona == a:
                self.lista_pedidos.remove(item)
                break
        self.lista_alumnos.remove(a)

    def EliminarProfesor(self,nombre,apellido):
        p=None
        for item in self.lista_profesores:
            if item.nombre == nombre and item.apellido == apellido:
                p = item
                break
        if not p:
            return False

        for item in self.lista_pedidos:
            if item.persona == p:
                self.lista_pedidos.remove(item)
                break
        self.lista_profesores.remove(p)

    def EliminarPlato(self,nombre_plato,precio):
        pl = None
        for item in self.lista_platos:
            if item.nombre == nombre_plato and item.precio == precio:
                pl = item
                break
        if not pl:
            return False

        for item in self.lista_pedidos:
            if item.plato == pl:
                self.lista_pedidos.remove(item)
                break
        self.lista_platos.remove(pl)

    def EliminarPedido(self,pe,pl):
        for item in self.lista_pedidos:
            if item.persona == pe and item.plato == pl:
                self.lista_pedidos.remove(item)

    def ModificarAlumno(self,A,nuevo_nombre,nuevo_apellido,nueva_division):
        A = Alumno()
        for item in self.lista_pedidos:
            if item.nombre == A.nombre and item.apellido == A.apellido:
                A.nombre = nuevo_nombre
                A.apellido = nuevo_apellido
                A.division = nueva_division

    def ModificarProfesor(self,Pr,nuevo_nombre,nuevo_apellido,nuevo_descuento):
        Pr = Profesor()
        for item in self.lista_profesores:
            if item.nombre == Pr.nombre and item.apellido == Pr.apellido:
                Pr.nombre = nuevo_nombre
                Pr.apellido = nuevo_apellido
                Pr.descuento = nuevo_descuento

    def ModificarPlato(self,Pl,nuevo_nombre_plato,nuevo_precio):
        Pl = Plato()
        for item in self.lista_pedidos:
            if item.nombre_plato == Pl.nombre_plato and item.precio == Pl.precio:
                Pl.nombre_plato = nuevo_nombre_plato
                Pl.precio = nuevo_precio
