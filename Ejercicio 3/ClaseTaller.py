class Taller:
    __idtaller = 0
    __nombre = ''
    __vacantes = 0
    __montoinscripcion = 0
    def __init__(self, idt:int, nomb:str, vacan:int, monto:int):
        self.__idtaller = idt
        self.__nombre = nomb
        self.__vacantes = vacan
        self.__montoinscripcion = monto

    def getnombre(self): return self.__nombre
    def getvacantes(self): return self.__vacantes
    def getmontoinscripcion(self): return self.__montoinscripcion
    def getidtaller(self): return self.__idtaller