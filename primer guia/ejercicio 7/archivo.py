from persona import Profesor
from persona import Alumno
from plato import Plato

L = []
P1 = Profesor("Roberto","Garcia")
P2 = Profesor("Gaspar", "Ramirez")
P3 = Profesor("Rodrigo", "Rodriguez")
L.append(P1)
L.append(P2)
L.append(P3)

L2 = []
A = Alumno("Javier","Gimenez","5C")
A2 = Alumno("Lucas","Braisen","1A")
A3 = Alumno("Ernesto","Hernandez","3B")

L2.append(A)
L2.append(A2)
L2.append(A3)

L3 = []
Pl1 = Plato("Costillas a la riojana",130)
Pl2 = Plato("Fideos con boloñesa",90)
Pl3 = Plato("Hamburguesa completa",85)
Pl4 = Plato("Tortilla de papa",55)
Pl5 = Plato("Milanesa de soja",70)
Pl6 = Plato("Ensalada rusa",55)

L3.append(Pl1)
L3.append(Pl2)
L3.append(Pl3)
L3.append(Pl4)
L3.append(Pl5)
L3.append(Pl6)

f = open("miArchivo","w")
f.write("Profesores:")
f.write('\n')
for item in L:
    f.write(item.nombre + "|" + item.apellido)
    f.write('\n')
f.write('\n')
f.write("Alumnos:")
f.write('\n')
for item2 in L2:
    f.write(item2.nombre + "|" + item2.apellido + "|" + item2.division)
    f.write('\n')
f.write('\n')
f.write("Platos:")
f.write('\n')
for item3 in L3:
    f.write(item3.nombre_plato + "|" + str(item3.precio))
    f.write('\n')
f.close()

f = open("miArchivo","r")
for line in f:
    print(line)
f.close()


