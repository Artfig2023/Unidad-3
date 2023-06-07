from ClaseColeccion import Coleccion

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.salir
        }

        self.__coll = Coleccion()
        self.__coll.cargaplanta()
        self.__coll.cargaexternos()
        self.__coll.cargacontratados()

    def opcion(self, op):
        func = self.__switcher.get(op, lambda:print('Opcion incorrecta'))
        func()

    def opcion1(self):
        self.__coll.registrarhoras()

    def opcion2(self):
        self.__coll.totaltarea()

    def opcion3(self):
        self.__coll.ayudaeconomica()

    def opcion4(self):
        self.__coll.mostrarempleados()

    def salir(self):
        print('Fin del programa')