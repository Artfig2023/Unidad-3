class Nodo:
    __agente = None
    __siguiente = None
    __posicion = 0
    def __init__(self, agente, xpos):
        self.__agente = agente
        self.__siguiente = None
        self.__posicion = xpos

    def getsiguiente(self): return self.__siguiente
    def getdato(self): return self.__agente
    def setsiguiente(self, sig): self.__siguiente = sig
    def getposicion(self): return self.__posicion
    def incrementaposicion(self): self.__posicion += 1