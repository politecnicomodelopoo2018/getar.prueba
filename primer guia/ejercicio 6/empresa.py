class Empresa(object):
    nombre = None

    def __init__(self):
        self.lista_autos = []
        self.lista_camionetas = []

    def AgregarAuto(self,unAuto):
        self.lista_autos.append(unAuto)

    def AgregarCamioneta(self,unaCamioneta):
        self.lista_camionetas.append(unaCamioneta)