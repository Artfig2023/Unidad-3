from ClaseCarrera import Carrera

class Facultad:
    __codigo = 0
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = 0
    __listacarreras = []
    def __init__(self, cod:int, nom:str, dir:str, loc:str, telef:int, lista):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dir
        self.__localidad = loc
        self.__telefono = telef
        self.__listacarreras = []
        for i in range(len(lista)):
            unacarrera = Carrera(lista[i][1], lista[i][2], lista[i][3], lista[i][4], lista[i][5])
            self.__listacarreras.append(unacarrera)

    def getnombre(self): return self.__nombre
    def getcarreras(self): return self.__listacarreras
    def getcodigo(self): return self.__codigo
    def getlocalidad(self): return self.__localidad