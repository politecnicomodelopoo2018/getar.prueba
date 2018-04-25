from cancion import Cancion

class Album(object):
    nombre_album = None

    def __init__(self):
        self.lista_canciones = []

    def setNombreAlbum(self,nombre_album):
        self.nombre_album = nombre_album

    def setAgregarCancion(self,titulo):
        C = Cancion()
        C.setTitulo(titulo)
        self.lista_canciones.append(C)

    def ArtistasQueParticipan(self):
        participantes = []
        for item in self.lista_canciones:
            for item2 in self.lista_artistas:
                if item2 not in self.participantes:
                    self.participantes.append(item2)
        return participantes

    def ArtistaMasInfluyente(self):
        influyentes = []
        influencia = 0
        influyente = None
        for item in self.lista_canciones:
            for item2 in self.lista_artistas:
                if item2 not in influyentes:
                    influyentes.append([item2,1])
                else:
                    for item3 in influyentes:
                        if item3 == item2:
                            influyentes[1] += 1
        for item4 in influyentes:
            if item4[1] > influencia:
                influencia = item4[1]
                influyente = item4[0]
        return influyente
