# pro = promedio

class Materia(object):
    nombre = None

    def __init__(self,nombre):
        self.nombre = nombre
        self.ListaNotas = []

    def __init__(self, notas):
        self.ListaNotas = []

    def AgregarNota(self, nota):
        if nota > 10:
            return False
        if nota < 1:
            return False
        self.ListaNotas.append(nota)
        return True

    def MenorNota(self):
        return min(self.ListaNotas)

    def MayorNota(self):
        return max(self.ListaNotas)

    def promedio(self):
        if len(self.ListaNotas) == 0:
            return False
        return sum(self.ListaNotas)/len(self.ListaNotas)