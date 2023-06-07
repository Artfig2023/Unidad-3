class Inscripcion:
    __fechainscripcion = ''
    __pago = None

    __taller = None
    __persona = None
    def __init__(self, fecha:str, pag:bool, per, tall):
        self.__fechainscripcion = fecha
        self.__pago = pag

        self.__persona = per
        self.__taller = tall

    def getpago(self): return self.__pago
    def getfecha(self): return self.__fechainscripcion

    def getpersona(self): return self.__persona
    def gettaller(self): return self.__taller

    def realizarpago(self):
        self.__pago == True