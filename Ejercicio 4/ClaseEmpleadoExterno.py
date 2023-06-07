from ClaseEmpleado import Empleado
from datetime import date

class Externo(Empleado):
    __tarea = ''
    __fechainicio = date
    __fechafin = date
    __montoviatico = 0.0
    __costobra = 0.0
    __montoseguro = 0.0
    def __init__(self, dni:int, nomb:str, direc:str, telef:int, tar:str, fechai:date, fechaf:date, mv:float,
                 co:float, ms:float):
        super().__init__(dni, nomb, direc, telef)
        self.__tarea = tar
        self.__fechainicio = fechai
        self.__fechafin = fechaf
        self.__montoviatico = mv
        self.__costobra = co
        self.__montoseguro = ms

    def gettarea(self): return self.__tarea
    def getfechainicio(self): return self.__fechainicio
    def getfechafin(self): return self.__fechafin
    def getviatico(self): return self.__montoviatico
    def getcostobra(self): return self.__costobra
    def getmontoseguro(self): return self.__montoseguro

    def calcularsueldo(self):
        sueldo = self.__costobra - self.__montoviatico - self.__montoseguro
        return sueldo