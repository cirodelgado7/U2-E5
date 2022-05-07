class PlanAhorro:
    __codigo = 0
    __modelo = ''
    __version = ''
    __valor = 0.0

    __cuotasPlan = 0
    __cuotasLicitar = 0

    def __init__(self, codigo=0, modelo='', version='', valor=0.0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version = version
        self.__valor = valor

    def __str__(self):
        return 'Codigo: {} \n Modelo: {} \n Version: {} Valor: {} \n Cuotas del Plan: {} \n Cuotas para licitar: {}'\
            .format(self.__codigo, self.__modelo, self.__version, self.__valor, PlanAhorro.getCuotasPlan(), PlanAhorro.getCuotasLicitar())

    @classmethod
    def getCuotasPlan(cls):
        return cls.__cuotasPlan

    @classmethod
    def setCuotasPlan(cls, c):
        cls.__cuotasPlan = c

    @classmethod
    def getCuotasLicitar(cls):
        return cls.__cuotasLicitar

    @classmethod
    def setCuotasLicitar(cls, c):
        cls.__cuotasLicitar = c