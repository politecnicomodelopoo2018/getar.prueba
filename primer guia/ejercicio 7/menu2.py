import os
from persona import Profesor
from persona import Alumno
from plato import Plato
from pedido import Pedido
from menu import Menu

M = Menu()

while(True):
    print("Bienvenido al Buffet, elija una opcion: ")
    print("1) Opciones de Alumno: ")
    print("2) Opciones de Profesor: ")
    print("3) Opciones de Plato: ")
    print("4) Opciones de Pedido: ")
    print("5) Salir")
    o = input("Opcion: ")

    if o == 1:
        os.system('clear')
        while(True):
            print("Opciones de Alumno:")
            print("1) Agregar Alumno ")
            print("2) Eliminar Alumno ")
            print("3) Modificar Alumno ")
            print("4) Salir")
            op = input("Opcion: ")

            if op == 1:
                os.system('clear')
                print("Agregar Alumno:")
                M.AgregarAlumno()
                print("Alumno agregado")

            if op == 2:
                os.system('clear')
                print("ELiminar Alumno:")
                M.EliminarAlumno()
                print("Alumno eliminado")

            if op == 3:
                os.system('clear')
                print("Modificar Alumno:")
                M.ModificarAlumno()
                print("Alumno modificado")

            if op == 4:
                break

    if o == 2:
        os.system('clear')
        while(True):
            print("Opciones de Profesor: ")
            print("1) Agregar Profesor")
            print("2) Eliminar Profesor")
            print("3) Modificar Profesor")
            print("4) Salir")
            op2 = input("Opcion: ")

            if op2 == 1:
                os.system('clear')
                print("Agregar Profesor")
                M.AgregarProfesor()
                print("Profesor agregado")

            if op2 == 2:
                os.system('clear')
                print("Eliminar Profesor")
                M.EliminarProfesor()
                print("Profesor eliminado")

            if op2 == 3:
                os.system('clear')
                print("Modificar Profesor")
                M.ModificarProfesor()
                print("Pofesor modificado")

    if o == 3:
        os.system('clear')
        while(True):
            print("Opciones de Plato: ")
            print("1) Agregar Plato")
            print("2) Eliminar Plato")
            print("3) Modificar Plato")
            print("4) Salir")
            op3 = input("Opcion:")

            if op3 == 1:
                os.system('clear')
                print("Agregar Profesor")
                M.AgregarProfesor()
                print("Profesor agregado")

            if op3 == 2:
                os.system('clear')
                print("Eliminar Profesor")
                M.EliminarProfesor()
                print("Profesor eliminado")

            if op3 == 3:
                os.system('clear')
                print("Modificar Profesor")
                M.ModificarProfesor()
                print("Pofesor modificado")



