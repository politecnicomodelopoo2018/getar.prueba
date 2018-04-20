from cancion import Cancion
from persona import Autor
from persona import Artista

class album(object):
    nombre_album = None

    def __init__(self):
        self.lista_canciones = []

    def setNombreAlbum(self,nombre_album):
        self.nombre_album = nombre_album

    def setAgregarCancion(self,C):
        self.lista_canciones.append(C)

    def ArtistasQueParticipan(self):
        self.participantes = []
        for item in self.lista_canciones:
            for item2 in self.lista_artistas:
                if item2 not in self.participantes:
                    self.participantes.append(item2)
        return participantes()

    def ArtistaMasInfluyente(self,nombre_artista):

