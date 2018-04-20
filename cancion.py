class Cancion(object):
    titulo = None

    def __init__(self):
        self.lista_autores = []
        self.lista_artistas = []

    def setTitulo(self,titulo):
        self.titulo = titulo

    def AgregarAutor(self,A):
        self.lista_autores.append(A)

    def AgregarArtista(self,Ar):
        self.lista_artistas.append(Ar)

