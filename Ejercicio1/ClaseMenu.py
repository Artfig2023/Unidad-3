from ClaseManejador import Manejador

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1':self.__opcion1,
            '2':self.__opcion2,
            '3':self.salir
        }

        self.__man = Manejador()
        self.__man.testfacultad()

    def opcion(self, op):
        func = self.__switcher.get(op, lambda:print('Error: Opcion incorrecta'))
        func()

    def salir(self):
        print('Fin del programa')

    def opcion1(self):
        cod = int(input('Ingrese codigo de Facultad: '))
        indice = self.__man.buscafacultad(cod)
        if indice != -1:
            self.__man.muestrafacu(indice)
        else:
            print('No se encontro Facultad')

    def opcion2(self):
        carrera = input('Ingrese nombre de una carrera: ')
        band = self.__man.muestracarrera(carrera)
        if band == False:
            print('Carrera no encontrada')