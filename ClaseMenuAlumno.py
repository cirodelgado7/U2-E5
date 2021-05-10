import sys
from ClaseManejadorAlumno import Manejador
from ClaseAlumno import Alumno

class Menu:

    __switcher = None

    def __init__(self):
        __switcher = None
        self.__switcher = {
            1: self.listar,
            2: self.modificar,
            3: self.salir
            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self,op,ma):
        func = self.__switcher.get(op,lambda: print("Opción no válida"))
        func(ma)

    def listar(self,ma):
        a = int(input('Año: '))
        d = input('División: ')
        Manejador.mostrar(ma,a,d)
        
    def modificar(self,ma):
        print('La cantidad actual de inasistencias permitidas es: {}'.format(Alumno.getPermitidas()))
        n = int(input('Ingrese la nueva cantidad de inasistencias permitidas: '))
        Alumno.setPermitidas(n)
        print('La nueva cantidad de inasistencias permitidas es: {}'.format(Alumno.getPermitidas()))

    def salir(self,ma):
        sys.exit(0)