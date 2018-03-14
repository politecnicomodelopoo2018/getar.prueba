class materia(object):
    nombre = None

    def __init__(self, notas):
        self.ListaNotas = []

    def AgregarNota(self, nota):
        if nota > 10:
            return False
        if nota < 1:
            return False
        self.ListaNotas.append(nota)
        return True


