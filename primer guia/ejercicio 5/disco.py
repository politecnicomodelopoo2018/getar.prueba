from album import Album


class Disco (object):
    nombre_disco = None

    def __init__(self):
        self.lista_albums = []

    def SetNombre_Disco(self,nombre_disco):
         self.nombre_disco = nombre_disco

    def AgregarAlbum(self,nombre_album):
        A = Album()
        A.setNombreAlbum(nombre_album)
        self.lista_albums.append(A)

    def CancionesAutorNacionalidad(self,nacionalidad):
        canciones_autor = []
        for item in self.lista_albums:
            for item2 in self.lista_canciones:
                for item3 in self.lista_autores:
                    if item3.nacionalidad == nacionalidad:
                        canciones_autor.append(item2)
        return canciones_autor
