import csv
from ClaseAlumno import Alumno

class Manejador:

    __listaAlumno = []

    def __init__(self):
        self.__listaAlumno = []

    def __str__(self):
        s = ""
        for lista in self.__listaAlumno:
            s += str(lista) + '\n'
        return s

    def testAlumnos(self):
        archivo = open('Alumnos.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
              nombre = fila[0]
              año = fila[1]
              division = fila[2]
              cantInas = fila[3]
              unAlumno = Alumno(nombre,año,division,cantInas)
              self.agregarAlumno(unAlumno)
        archivo.close()

    def agregarAlumno(self,unAlumno):
        self.__listaAlumno.append(unAlumno)

    def obtenerAlumno(self, indice):
        return self.__listaAlumno[indice]

    def mostrar(self, a, d):
        print('\n %15s %33s' % ('Alumno/a','Porcentaje'))
        for i in self.__listaAlumno:
            if (int(Alumno.getAño(i)) == a) and (Alumno.getDivision(i) == d.upper()) and int(Alumno.getCantInasisitencias(i)) > Alumno.getPermitidas():
                print('{:40}  {:.2f}%'.format(Alumno.getNombre(i),(float((int(Alumno.getCantInasisitencias(i))*100)/int(Alumno.cantInasPermitidas)))))