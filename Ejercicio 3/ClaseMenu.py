from ClaseManejoInscripcion import  ManejoInscripcion

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.opcion5,
            '6': self.salir
        }

        self.__mins = ManejoInscripcion()

    def opcion(self, op):
        func = self.__switcher.get(op, lambda:print('Error - Opcion incorrecta'))
        func()

    def opcion1(self):
        self.__mins.inscripcion()

    def opcion2(self):
        self.__mins.consultainscripcion()

    def opcion3(self):
        self.__mins.listarinscriptos()

    def opcion4(self):
        self.__mins.verificarpago()

    def opcion5(self):
        self.__mins.guardarinscripciones()

    def salir(self):
        print('Fin del programa')