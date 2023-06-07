from ClaseSabor import Sabor

class Helado:
    __gramos = float
    __precio = float
    __sabores = None
    def __init__(self, gram:float, pre:float):
        self.__gramos = gram
        self.__precio = pre

    def getgramos(self): return self.__gramos
    def getprecio(self): return self.__precio
    def getsabores(self): return self.__sabores

    def cargalistasabor(self, lissabor:Sabor):
        self.__sabores.append(lissabor)