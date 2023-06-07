class Carrera:
    __codigo = 0
    __nombre = ''
    __fechainicio = ''
    __duracion = ''
    __titulo = ''
    def __init__(self, cod:int, nom:str, fech:str, dur:str, tit:str, tip:str):
        self.__codigo = cod
        self.__nombre = nom
        self.__fechainicio = fech
        self.__duracion = dur
        self.__titulo = tit
        self.__tipo = tip

    def __str__(self):
        return 'Nombre: ' + self.__nombre + ' - Duracion: ' + self.__duracion

    def getnombre(self): return self.__nombre
    def getcodigo(self): return self.__codigo