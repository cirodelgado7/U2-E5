class Alumno:
    __nombre = ''
    __año = ''
    __division = ''
    __cantInasistencias = 0

    cantInasPermitidas = 10
    cantTotalClases = 0

    def __init__(self, nombre = '', año = '', division = '', cantInasistencias = 0):
        self.__nombre = nombre
        self.__año = año
        self.__division = division
        self.__cantInasistencias = cantInasistencias

    def __str__(self):
        return '{:40}   {}\t\t   {}\t\t   {}\t\t' .format(self.__nombre, self.__año , self.__division, self.__cantInasistencias)

    def getNombre(self):
        return self.__nombre

    def getAño(self):
        return self.__año

    def getDivision(self):
        return self.__division

    def getCantInasisitencias(self):
        return self.__cantInasistencias

    @classmethod
    def getPermitidas(cls):
        return cls.cantInasPermitidas

    @classmethod
    def setPermitidas(cls, c):
        cls.cantInasPermitidas = c

    @classmethod
    def getTotal(cls):
        return cls.cantTotalClases