import abc
from abc import ABC


class Empleado(ABC):
    _dni = ''
    _nombre = ''
    _direccion = ''
    _telefono = ''

    def __init__(self, dni, nom, dir, tel):
        self._dni = dni
        self._nombre = nom
        self._direccion = dir
        self._telefono = tel

    def getdni(self): return self._dni

    def getdir(self): return self._direccion

    def getnom(self): return self._nombre

    def gettel(self): return self._telefono

    def mostrarempleado(self):
        print('DNI: '.format(self._dni))
        print('Nombre: '.format(self._nombre))
        print('Direccion: '.format(self._direccion))
        print('Telefono: '.format(self._telefono))

    @abc.abstractmethod
    def calcSueldo(self):
        pass

    @abc.abstractmethod
    def getTipo(self):
        pass