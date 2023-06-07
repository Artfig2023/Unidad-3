from ClaseEmpleado import Empleado

class Planta(Empleado):
    __sueldobasico = 0.0
    __antiguedad = 0

    def __init__(self, dni, nom, dir, tel, basic, anti):
        super().__init__(dni, nom, dir, tel)
        self.__sueldobasico = basic
        self.__antiguedad = anti

    def mostrarempleado(self):
        super().mostrarempleado()
        print('Condicion: '.format('Planta'))
        print('Sueldo basico: $'.format(str(self.__sueldoBasico)))
        print('Antiguedad: '.format(str(self.__antiguedad)))

    def calcSueldo(self):
        sueldo = self.__sueldobasico * (1 + 0.01 * self.__antiguedad)
        sueldo = round(sueldo, 2)
        return sueldo

    def setbasico(self, nbasico):
        self.__sueldobasico = nbasico

    def getTipo(self):
        return 'Planta'