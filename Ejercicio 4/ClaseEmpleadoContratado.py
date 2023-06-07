from ClaseEmpleado import Empleado
from datetime import date

class Contratado(Empleado):
    __fechainicio = date
    __fechafin = date
    __canthoras = 0
    __valorhora = 3000.0
    def __init__(self, dni:int, nomb:str, direc:str, telef:int, fechai:date, fechaf:date, horas:int):
        super().__init__(dni, nomb, direc, telef)
        self.__fechainicio = fechai
        self.__fechafin = fechaf
        self.__canthoras = horas

    def getfechainicio(self): return self.__fechainicio
    def getfechafin(self): return self.__fechafin
    def sethoras(self, horas): self.__canthoras += horas

    @classmethod
    def getvalorhora(cls):
        return cls.__valorhora

    def calcularsueldo(self):
        sueldo = self.__canthoras * self.__valorhora
        return sueldo