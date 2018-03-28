from equipo import Equipo
from jugador import Jugador
from Campeonato import campeonato
import datetime

j = Jugador()
j.setCapitan(True)
j.setNumeroCamiseta(1)
j.setNombreJugador("Pepe")
j.setFechaNacimiento(datetime.date(1999,10,1))

a = Jugador()
a.setCapitan(False)
a.setNumeroCamiseta(2)
a.setNombreJugador("Enzo")
a.setFechaNacimiento(datetime.date(1999,11,11))

h = Jugador()
h.setCapitan(False)
h.setNumeroCamiseta(3)
h.setNombreJugador("Pablo")
h.setFechaNacimiento(datetime.date(1999,1,29))

eq = Equipo()
eq.nombre_equipo="Manuel Belgrano"
eq.barrio="Saavedra"
eq.ListaJugadores.append(j)
eq.ListaJugadores.append(a)
eq.ListaJugadores.append(h)

#for item in eq.ListaJugadores:
#   print("%s %d" % (item.nombre_jugador,item.numero_camiseta))
#   print(item.fecha_nacimiento)

cl = campeonato()
