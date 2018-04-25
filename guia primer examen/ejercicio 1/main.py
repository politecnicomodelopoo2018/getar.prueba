from Persona import persona
import datetime

p = persona()
p.setNombre("Carlos")
p.setApellido("Velasquez")
p.setFecha_Nacimiento(datetime.date(1990,1,11))

p.AgregarChequeo(66,165,datetime.date(2008,10,12))
p.AgregarChequeo(65,163,datetime.date(2008,1,12))
p.AgregarChequeo(67,164,datetime.date(2008,5,19))
p.AgregarChequeo(94,180,datetime.date(2017,10,2))
p.AgregarChequeo(90,179,datetime.date(2017,1,2))
#print(p.PromedioPeso(2008))
#print(p.PromedioAltura(2008))
#print(p.PromedioAltura(2017))
print(p.BuscarChequeo(datetime.date(2008,5,19)).peso)

#print(p.PorcentajeCrecimiento(2008,2017))




