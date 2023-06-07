from ClaseManejador import Manejador
from Interfaces import Iinterface
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
            '9': self.opcion9,
            '10': self.salir
        }

        self.__json = ObjectEncoder()
        self.__man = Manejador()
        self.__inter = Iinterface()

    def opcion(self, op):
        func = self.__switcher.get(op, lambda:print('Error. opcion incorrecta'))
        func()

    def opcion1(self):
        band = False
        agente = self.__man.cargaunagente()
        while not band:
            try:
                posicion = int(input('Ingrese posicion a insertar: '))
                assert type(posicion) is int, 'Debe ser un numero entero'
                assert posicion > 0, 'Debe ser un numero positivo mayor a 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        self.__inter.insertarElemento(agente, posicion)

    def opcion2(self):
        agente = self.__man.cargaunagente()
        self.__inter.agregarElemento(agente)

    def opcion3(self):
        band = False
        while not band:
            try:
                posicion = int(input('Ingrese posicion a insertar: '))
                assert type(posicion) is int, 'Debe ser un numero entero'
                assert posicion > 0, 'Debe ser un numero positivo mayor a 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        self.__inter.mostrarElemento(posicion)

    def opcion4(self):
        carrera = input('Ingrese carrera: ')
        print('Carrera ingresada: {}', carrera)
        self.__man.listardocentesinvestgador(carrera)

    def opcion5(self):
        area = input('Ingrese area de investigacion: ')
        print('Area ingresada: {}', area)
        print('Cantidad de agentes encontrados')
        self.__man.contararea(area)

    def opcion6(self):
        self.__man.listartodosagentes()

    def opcion7(self):
        band = False
        while not band:
            try:
                categ = input('Ingrese categoria (I, II, III, IV, V): ')
                categ.upper()
                assert len(categ) <= 3, 'Debe ingresar 3 caracteres o menos'
                assert categ == 'I' or categ == 'II' or categ == 'III' or categ == 'IV' or categ == 'V'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        self.__man.mostrardocentes(categ)

    def opcion8(self):
        d = self.__man.toJSON()
        self.__json.guardarJSON(d, 'personal.json')
        print('Se guardo el archivo JSON')

    def opcion9(self):
        diccionario = self.__json.leerJSON('personal.json')
        self.__man = self.__json.decodificarDiccionario(diccionario)
        self.__inter = Iinterface(self.__man)
        print('Se ha cargado el archivo JSON')

    def salir(self):
        print('Fin del programa')