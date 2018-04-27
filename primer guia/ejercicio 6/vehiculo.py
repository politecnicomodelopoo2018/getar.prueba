class Vehiculo(object):
    patente = None
    cantidad_ruedas = None
    fecha_fabricacion = None

    def setPatente(self,patente):
        self.patente = patente

    def setRuedas(self,cantidad_ruedas):
        self.cantidad_ruedas = cantidad_ruedas

    def setFechaFabricacion(self,fecha_fabricacion):
        self.fecha_fabricacion = fecha_fabricacion

class Auto(Vehiculo):
    descapotable = None

    def setDescapotable(self,descapotable):
        self.descapotable = descapotable

class Camioneta(Vehiculo):
    capacidad_carga = None

    def setCapacidad(self,capacidad_carga):
        self.capacidad_carga = capacidad_carga