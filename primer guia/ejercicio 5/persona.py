class Persona(object):
    nombre = None
    apellido = None
    fecha_nacimiento = None

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellido(self,apellido):
        self.apellido = apellido

    def setFecha_Nacimiento(self,fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

class Autor(Persona):
    nacionalidad = None

    def setNacionalidad(self,nacionalidad):
        self.nacionalidad = nacionalidad

class Artista(Persona):
    pass