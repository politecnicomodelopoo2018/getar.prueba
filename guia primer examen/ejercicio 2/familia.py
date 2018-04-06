from persona import Persona

class familia(object):
    nombre = None

    def __init__(self):
        self.familiares = []

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def AgregarFamiliar(self,apellido,fecha_nacimiento):
        F = Persona()
        F.setApellido(apellido)
        F.setFechaNacimiento(fecha_nacimiento)
        self.familiares.append(F)

    def PromedioCaloriasFamilia(self):
        cantidad_familiares = 0
        prom_calorias = 0
        for item in self.familiares:
            prom_calorias += item.SumaCalorias()
            cantidad_familiares += 1
            if cantidad_familiares == 0:
                return None
        return prom_calorias/cantidad_familiares

    def FamiliarQueComeMasCalorias(self):
        MayorCalorias = 0
        p = None
        for item in self.familiares:
            if item.SumaCalorias() > MayorCalorias:
                MayorCalorias = item.SumaCalorias()
                p = item
        return MayorCalorias, p

    def FamiliarQueComeMenosCalorias(self):
        MenorCalorias = self.familiares[0].sumaCalorias()
        p= self.familiares[0]
        for item in self.familiares:
            if item.SumaCalorias() < MenorCalorias:
                MenorCalorias = item.SumaCalorias()
                p = item
        return MenorCalorias, p




