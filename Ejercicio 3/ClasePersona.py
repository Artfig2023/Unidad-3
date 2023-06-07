class Persona:
    __nombre = ''
    __direccion = ''
    __dni = 0
    def __init__(self, nomb:str, dir:str, dn:int):
        self.__nombre = nomb
        self.__direccion = dir
        self.__dni = dn

    def getdni(self): return self.__dni

    def __str__(self):
        return 'Nombre: {}' + self.__nombre + ' /Direccion: {}' + self.__direccion + ' /DNI: {}' + self.__dni