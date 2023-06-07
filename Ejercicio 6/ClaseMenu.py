from Interface import Iinterface
from ClaseManejadorVehiculo import ManejoVehiculo
from ClaseObjectEncoder import ObjectEncoder

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.opcion5,
            '6': self.opcion6,
            '7': self.opcion7,
            '8': self.opcion8,
            '9': self.salir
        }

        self.__json = ObjectEncoder()
        self.__man = ManejoVehiculo()
        self.__inter = Iinterface()

    def opcion(self, op):
        func = self.__switcher.get(op, lambda: print('Opcion incorrecta'))
        func()

    def opcion1(self):
        band = False
        vehiculo = self.__man.crearvehiculo()
        self.__inter.agregarElemento(vehiculo)

    def opcion2(self):
        band = False
        vehiculo = self.__man.crearvehiculo()
        while not band:
            try:
                pos = int(input('Ingrese posicion: '))
                assert type(pos) is int, "Debe ingresar un numero entero"
                assert pos > 0, "Debe ingresar un numero positivo"
            except:
                print('Error. Ingrese un valor valido')
            else:
                band = True
        self.__inter.insertarElemento(vehiculo, pos)

    def opcion3(self):
        band = False
        while not band:
            try:
                pos = int(input('Ingrese posicion'))
                assert type(pos) is int, "Debe ingresar un numero entero"
                assert pos > 0, "Debe ingresar un numero positivo"
            except:
                print('Error. Ingrese un valor valido')
            else:
                band = True
        self.__inter.mostrarElemento(pos)

    def opcion4(self):
        self.__man.modificaprecio()

    def opcion5(self):
        self.__man.muestraeco()

    def opcion6(self):
        self.__man.listavehiculos()

    def opcion7(self):
        d = self.__man.toJSON()
        self.__json.guardarJSONarchivo(d, 'Vehiculos.json')
        print('Datos de vehiculos guardados en el archivo .json')

    def opcion8(self):
        diccionario = self.__json.leerJSONarchivo('Vehiculos.json')
        self.__man = self.__json.decodificadordiccionario(diccionario)
        self.__inter = Iinterface(self.__man)
        print('Se cargo los datos del archivo .json')

    def salir(self):
        print('Fin del programa')