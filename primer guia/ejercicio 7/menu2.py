import os
from persona import Profesor
from persona import Alumno
from plato import Plato
from pedido import Pedido
from clase_menu import Menu

M = Menu()

while(True):
    print("Bienvenido al Buffet, elija una opcion: ")
    print("1) Opciones de Alumno: ")
    print("2) Opciones de Profesor: ")
    print("3) Opciones de Plato: ")
    print("4) Opciones de Pedido: ")
    print("5) Salir")
    o = input("Opcion: ")

    if o == "1":
        os.system('clear')
        while(True):
            print("Opciones de Alumno:")
            print("1) Agregar Alumno ")
            print("2) Eliminar Alumno ")
            print("3) Modificar Alumno ")
            op = input("Opcion: ")

            if op == "1":
                os.system('clear')
                print("Agregar Alumno:")
                M.AgregarAlumno()
                os.system('clear')

            if op == "2":
                os.system('clear')
                print("ELiminar Alumno:")
                M.EliminarAlumno()
                os.system('clear')

            if op == "3":
                os.system('clear')
                print("Modificar Alumno:")
                M.ModificarAlumno()
                print("Alumno modificado")

            else:
                break

    if o == "2":
        os.system('clear')
        while(True):
            print("Opciones de Profesor: ")
            print("1) Agregar Profesor")
            print("2) Eliminar Profesor")
            print("3) Modificar Profesor")
            op2 = input("Opcion: ")

            if op2 == "1":
                os.system('clear')
                print("Agregar Profesor")
                M.AgregarProfesor()
                print("Profesor agregado")

            if op2 == "2":
                os.system('clear')
                print("Eliminar Profesor")
                M.EliminarProfesor()
                print("Profesor eliminado")

            if op2 == "3":
                os.system('clear')
                print("Modificar Profesor")
                M.ModificarProfesor()
                print("Pofesor modificado")

            else:
                break

    if o == "3":
        os.system('clear')
        while(True):
            print("Opciones de Plato:")
            print("1) Agregar Plato")
            print("2) Eliminar Plato")
            print("3) Modificar Plato")
            op3 = input("Opcion: ")

            if op3 == "1":
                os.system('clear')
                print("Agregar Profesor")
                M.AgregarProfesor()
                print("Profesor agregado")

            if op3 == "2":
                os.system('clear')
                print("Eliminar Profesor")
                M.EliminarProfesor()
                print("Profesor eliminado")

            if op3 == "3":
                os.system('clear')
                print("Modificar Profesor")
                M.ModificarProfesor()
                print("Pofesor modificado")

            else:
                break

    if o == "4":
        os.system('clear')
        while(True):
            print("Opciones de Pedido:")
            print("1) Agregar Pedido")
            print("2) Eliminar Pedido")
            print("3) Modificar Pedido")
            op4 = input("Opcion: ")

            if op4 == "1":
                os.system('clear')
                print("Agregar Pedido")
                M.AgregarPedido()
                print("Pedido agregado")

            if op4 == "2":
                os.system('clear')
                print("Eliminar Pedido")
                M.EliminarPedido()
                print("Pedido eliminado")

            if op4 == "3":
                os.system('clear')
                print("Modificar Pedido")
                M.Modificar()




