# coding=utf-8
import Empresa
import datetime

E = Empresa.empresa()
E.setNombre("Prusci.SA")
E.AñadirEmpleado("Gonzalo","Gonzales",datetime.date(1990-1-1),"15-5854-5670")
E.AñadirEmpleado("Rigoberto","Sujari",datetime.date(1981-1-1),"15-2223-4536")
E.AñadirEmpleado("Ramon","Barragan",datetime.date(1997-6-9),"15-1122-0980")

f = open("archivo relampago","w")
f.write("Empleados:")
f.write('\n')
for item in E.ListaE:
    f.write(item)
    f.witr('\n')
f.close()


