class Empleado:
    __dni = 0
    __nombre = ''
    __direccion = ''
    __telefono = 0
    def __init__(self, dni:int, nom:str, dire:str, tele:int):
        self.__dni = dni
        self.__nombre = nom
        self.__direccion = dire
        self.__telefono = tele

    def getdni(self): return self.__dni
    def getnombre(self): return self.__nombre
    def getdireccion(self): return self.__direccion
    def gettelefono(self): return self.__telefono