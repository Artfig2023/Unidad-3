import abc

class Agente(abc):
    __cuil = 0
    __apellido = ''
    __nombre = ''
    __sueldobasico = 0.0
    __antiguedad = 0
    def __init__(self, cui:int, apel, nom, sueb:float, anti:int):
        self.__cuil = cui
        self.__apellido = apel
        self.__nombre = nom
        self.__sueldobasico = sueb
        self.__antiguedad = anti

    def getcuil(self): return self.__cuil
    def getapellido(self): return self.__apellido
    def getnombre(self): return self.__nombre
    def getsueldobasico(self): return self.__sueldobasico
    def getantiguedad(self): return self.__antiguedad

    def __str__(self):
        return 'Apellido: ' + self.__apellido + ' /Nombre: ' + self.__nombre