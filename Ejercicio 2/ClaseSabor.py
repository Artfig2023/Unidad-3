class Sabor:
    __idsabor = 0
    __ingredientes = ''
    __nombresabor = ''
    __acum = 0

    def __init__(self, ids:int, ingred:str, nombs:str):
        self.__idsabor = ids
        self.__ingredientes = ingred
        self.__nombresabor = nombs

    def getidsabor(self): return self.__idsabor
    def getingredientes(self): return self.__ingredientes
    def getnombresabor(self): return self.__nombresabor
    def sumaacum(self): self.__acum += 1
    def getacum(self): return self.__acum