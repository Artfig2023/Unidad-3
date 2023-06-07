from ClaseVehiculoUsado import Usado
from ClaseVehiculoNuevo import Nuevo
from ClaseLista import Lista
from zope.interface import implementer
from Interface import Iinterface

@implementer(Iinterface)

class ManejoVehiculo:
    __listavehiculos = None

    def __iter__(self):
        self.__listavehiculos = Lista

    def crearvehiculo(self):
        mod = input('Ingrese modelo:')
        cpuer = int('Ingrese cantidad de puertas:')
        color = input('Ingrese color:')
        precio = float(input('Ingrese precio base:'))
        op = int(input('¿Es un vehiculo nuevo? 1- Si. 2- No.'))
        assert type(op) is int, "Debe ingresar un numero entero"
        assert op >=1 and op <= 2, "Debe ingresar un numero indicado"
        if op == 1:
            ver = input('Ingrese version: (Base/Full):')
            unVehiculo = Nuevo(mod, cpuer, color, precio, ver)
            self.__listavehiculos.agregarvehiculo(unVehiculo)
        elif op == 2:
            marc = input('Ingrese marca:')
            pat = input('Ingrese patente:')
            an = int(input('Ingrese anho:'))
            km = float(input('Ingrese kilometraje:'))
            unVehiculo = Usado(mod, cpuer, color, precio, marc, pat, an, km)
            self.__listavehiculos.agregarvehiculo(unVehiculo)

    def agregarElemento(self, unvehiculo):
        self.__listavehiculos.agregarvehiculo(unvehiculo)
        print('Vehiculo agregado')

    def insertarElemento(self, unvehiculo, xpos):
        self.__listavehiculos.insertarvehiculo(unvehiculo, xpos - 1)

    def mostrarElemento(self, xpos):
        dato = self.__listavehiculos(xpos)
        if dato != None:
            if isinstance(dato, Nuevo):
                print('Posicion: ', xpos)
                print('Tipo de vehiculo: Nuevo')
            elif isinstance(dato, Usado):
                print('Posicion: ', xpos)
                print('Tipo de vehiculo: Usado')
        else:
            print('No se encontro algun elemento en la posicion ', xpos)

    def modificaprecio(self):
        pat = input('Ingrese patente: ')
        self.__listavehiculos.modificarpreciousado(pat)

    def muestraeco(self):
        self.__listavehiculos.mostrareconomico()

    def listavehiculos(self):
        self.__listavehiculos.mostrarvehiculos()

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributo__=[vehiculo.toJSON() for vehiculo in self.__listavehiculos]
        )
        return d