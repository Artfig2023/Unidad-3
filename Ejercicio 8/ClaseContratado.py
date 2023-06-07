from ClaseEmpleado import Empleado

class Contratado(Empleado):
    __fechainicio = None
    __fechafin = None
    __canthoras = 0
    __valorhora = 0
    valorhora = 500

    def __init__(self, dni, nom, dir, tel, fin, ffi, canth):
        super().__init__(dni, nom, dir, tel)
        self.__fechainicio = fin
        self.__fechafin = ffi
        self.__canthoras = canth
        self.__valorhora = self.valorhora

    def mostrarempleado(self):
        super().mostrarempleado()
        print('Condicion: '.format('Contratado'))
        print('Valor hora: '.format(str(self.__valorhora)))
        print('Inicio contrato: '.format(str(self.__fechainicio)))
        print('Fin contrato: '.format(str(self.__fechafin)))
        print('Horas trabajadas: '.format(str(self.__canthoras)))

    def addhora(self, horas):
        try:
            horas = int(horas)
            self.__canthoras += horas
            print('Horas agregadas')
        except:
            print('Error: La cantidad de horas debe ser entero')

    def calcularsueldo(self):
        sueldo = self.__canthoras * self.__valorhora
        return sueldo

    def getTipo(self): return 'Contratado'

    def setvalorhora(self, nuevovalor):
        self.__valorhora = nuevovalor