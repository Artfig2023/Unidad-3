from ClaseEmpleado import Empleado

class Externo(Empleado):
    __tarea = ''
    __fechainicio = None
    __fechafin = None
    __viatico = 0.0
    __costobra = 0.0
    __montoseguro = 0.0

    def __init__(self, dni, nom, dir, tel, tarea, fin, ffi, via, cost, mont):
        super().__init__(dni, nom, dir, tel)
        self.__tarea = tarea
        self.__fechainicio = fin
        self.__fechafin = ffi
        self.__viatico = via
        self.__costobra = cost
        self.__montoseguro = mont

    def mostrarempleado(self):
        super().mostrarempleado()
        print('Condicion: '.format('Externo'))
        print('Tarea: '.format(self.__tarea))
        print('Inicio tarea: '.format(str(self.__fechainicio)))
        print('Fin tarea: '.format(str(self.__fechafin)))
        print('Monto viatico: $'.format(str(self.__viatico)))
        print('Costo obra : $'.format(str(self.__costobra)))
        print('Monto seguro : $'.format(str(self.__montoseguro)))

    def gettarea(self): return self.__tarea
    def getfechainicio(self): return self.__fechainicio
    def getfechafin(self): return self.__fechafin
    def getviatico(self): return self.__viatico
    def getcostoobra(self): return self.__costobra
    def getmontoseguro(self): return self.__montoseguro

    def calcularsueldo(self):
        sueldo = self.__costobra - self.__viatico - self.__montoseguro
        return sueldo

    def setviatico(self, nuevia):
        self.__viatico = nuevia

    def gettipo(self):
        return 'Externo'