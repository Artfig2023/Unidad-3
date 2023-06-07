import abc
from abc import ABC

class Vehiculo:
    __modelo = ''
    __cantpuertas = 0
    __color = ''
    __preciobase = 0.0
    def __init__(self, mod:str, cant:int, col:str, pre:float):
        self.__modelo = mod
        self.__cantpuertas = cant
        self.__color = col
        self.__preciobase = pre

    def getprecio(self): return self.__preciobase
    def getpuertas(self): return self.__cantpuertas
    def getmodelo(self): return self.__modelo
    def getcolor(self): return self.__color

    def setprecio(self, precio): self.__preciobase = precio

    @abc.abstractmethod
    def toJSON(self):
        pass