from ClaseNodo import Nodo
from ClaseVehiculoNuevo import Nuevo
from ClaseVehiculoUsado import Usado

class Lista:
    __comienzo = Nodo
    __actual = Nodo
    __indice = 0
    __tope = 0

    __numnodos = 0

    def __init__(self):
        self.__comienzo = Nodo
        self.__actual = Nodo
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            vehiculo = self.__actual.getvehiculo()
            self.__actual = self.__actual.getsiguiente()
            return vehiculo

    def agregarvehiculo(self, unvehiculo):
        nodo = Nodo(unvehiculo, self.__numnodos)
        self.__numnodos += 1
        nodo.setsiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertarvehiculo(self, unvehiculo, xpos):
        band = False
        aux = self.__comienzo
        anterior = aux
        if xpos < self.__tope:
            while aux != None and band == False:
                if aux.getposicion() == xpos:
                    nodo = Nodo(unvehiculo, xpos)
                    anterior.setsiguiente(nodo)
                    aux.incrementaposicion()
                    nodo.setsiguiente(aux)
                    band = True
                    self.__tope += 1
                else:
                    anterior = aux
                    aux = aux.getsiguiente()
            while aux != None and aux.getposicion() < self.__tope:
                aux.incrementaposicion()
                aux = aux.getsiguiente()

    def buscaposicion(self, xpos):
        aux = self.__comienzo
        band = False
        dato = None
        if xpos < self.__tope:
            while aux != None and band == False:
                if aux.getposicion() == xpos:
                    dato = aux.getvehiculo()
                    band = True
                else:
                    aux = aux.getsiguiente()
        return dato

    def modificarpreciousado(self, pat):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if isinstance(aux.getvehiculo(), Usado):
                if aux.getvehiculo().getpatente() == pat:
                    nuevoprecio = float(input('Ingrese nuevo valor del vehiculo: '))
                    aux.setprecio(nuevoprecio)
                    band = True
                else:
                    aux = aux.getsiguiente()
        if band == False:
            print('Error. La patente no corresponde a un vehiculo cargado')

    def mostrareconomico(self):
        preciomin = self.__comienzo.getvehiculo().getprecio()
        vehiculoeco = self.__comienzo.getvehiculo()
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getvehiculo().getprecio() < preciomin:
                preciomin = aux.getvehiculo().getprecio()
                vehiculoeco = aux.getvehiculo()
                vehiculoeco.mostrar()
            if isinstance(vehiculoeco, Usado):
                print('Tipo de vehiculo: Usado')
                vehiculoeco.mostrar()
                band = True
            elif isinstance(vehiculoeco, Nuevo):
                print('Tipo de vehiculo: Nuevo')
                vehiculoeco.mostrar()
                band = True
            else:
                aux = aux.getsiguiente()

    def mostrarvehiculos(self):
        aux = self.__comienzo
        while aux != None:
            if isinstance(aux.getvehiculo(), Nuevo):
                print('Tipo de vehiculo: Nuevo')
            else:
                print('Tipo de vehiculo: Usado')
            print('Modelo: ', aux.getvehiculo().getmodelo())
            print('Cantidad de puertas: ', aux.getvehiculo().getpuertas())
            print('Importe de venta: $', aux.getvehiculo().calcularimporte())
            aux = aux.getsiguiente()