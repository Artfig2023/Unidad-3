from ClaseAgente import Agente

class Docente(Agente):
    __carrera = ''
    __cargo = ''
    __catedra = ''
    def __init__(self, cui:int, apel, nom, sueb:float, anti:int, carr, carg, cate):
        super().__init__(cui, apel, nom, sueb, anti)
        self.__carrera = carr
        self.__cargo = carg
        self.__catedra = cate

    def getcarrera(self): return self.__carrera
    def getcargo(self): return self.__cargo
    def getcatedra(self): return self.__catedra

    def __str__(self):
        return super().__str__() + ' /Carrera : ' + self.__carrera + ' /Cargo: ' + self.__cargo + ' /Catedra: ' + self.__catedra

    def calculaSueldo(self):
        porcen_antiguedad = ((super().getsueldobasico() * super().getantiguedad()) / 100)
        porcen_cargo = 0
        if self.__cargo == 'simple':
            porcen_cargo = ((super().getsueldobasico() * 10) / 100)
        elif self.__cargo == 'semiexclusivo':
            porcen_cargo = ((super().getsueldobasico() * 20) / 100)
        elif self.__cargo == 'exclusivo':
            porcen_cargo = ((super().getsueldobasico() * 50) / 100)
        total = super().getsueldobasico() + porcen_cargo + porcen_antiguedad
        return total

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getcuil(),
                apellido=super().getapellido(),
                nombre=super().getnombre(),
                sueldobasico=super().getsueldobasico(),
                antiguedad=super().getantiguedad(),
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return d