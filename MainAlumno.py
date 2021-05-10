from ClaseManejadorAlumno import Manejador
from ClaseMenuAlumno import Menu

if __name__ == '__main__':
    ma = Manejador()
    ma.testAlumnos()
    print(ma)
    menu = Menu()
    salir = False
    while not salir:
        print("\n-----------------Menu--------------------")
        print("1 - Listar nombres y porcentajes")
        print("2 - Modificar la cantidad máxima de inasistencias permitidas")
        print("3 - Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, ma)