from zope.interface import Interface

class Iinterface(Interface):

    def insertarElemento(self, elem, xpos):
        pass

    def agregarElemento(self, elem):
        pass

    def mostrarElemento(self, elem):
        pass