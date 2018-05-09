from programa import Programa
from musica import Musica

class Programa_Musical(Programa):
    musicalizador = None

    def __init__(self,musicalizador):
        self.musicalizador = musicalizador
        self.lista_musica = []

    def AgregarTipoMusica(self,nombre):
         M = Musica()
         M.nombre = nombre
         self.lista_musica.append(M)