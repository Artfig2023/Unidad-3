from zope.interface import interface

class Iinterface(interface):

    def insertarElemento(self, elem, xpos):
        pass

    def agregarElemento(self, elem):
        pass

    def mostrarElemento(self, xpos):
        pass