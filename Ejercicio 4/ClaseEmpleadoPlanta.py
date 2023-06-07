from ClaseEmpleado import Empleado

class Planta(Empleado):
    __sueldobasico = 0.0
    __antiguedad = 0
    def __init__(self, dni:int, nomb:str, direc:str, telef:int, sueb:float, anti:int):
        super().__init__(dni, nomb, direc, telef)
        self.__sueldobasico = sueb
        self.__antiguedad = anti

    def getsueldobasico(self): return self.__sueldobasico
    def getantiguedad(self): return self.__antiguedad

    def calcularsueldo(self):
        sueldo = self.__sueldobasico + (self.__sueldobasico / 100) * self.__antiguedad
        return sueldo