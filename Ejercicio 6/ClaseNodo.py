class Nodo:
    __vehiculo = None
    __siguiente = None

    __posicion = 0
    def __init__(self, unvehiculo, num):
        self.__vehiculo = unvehiculo
        self.__siguiente = None
        self.__posicion = num

    def getsiguiente(self): return self.__siguiente
    def getvehiculo(self): return self.__vehiculo

    def setsiguiente(self, sig): self.__siguiente = sig

    def getposicion(self): return self.__posicion
    def incrementaposicion(self): self.__posicion += 1