from ClaseAgente import Agente

class Investigador(Agente):
    __areainvestigacion = ''
    __tipoinvestigacion = ''
    def __init__(self, cui:int, apel, nom, sueb:float, anti:int, areai, tipoi):
        super().__init__(cui, apel, nom, sueb, anti)
        self.__areainvestigacion = areai
        self.__tipoinvestigacion = tipoi

    def getarea(self): return self.__areainvestigacion
    def gettipo(self): return self.__tipoinvestigacion

    def __str__(self):
        return super().__str__() + ' /Area de Investigacion: ' + self.__areainvestigacion + ' /Tipo de investigacion: ' + self.__tipoinvestigacion

    def calculaSueldo(self):
        porcen_antig = ((super().getSueldoBasico() * super().getAntiguedad()) / 100)
        total = super().getSueldoBasico() + porcen_antig
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
                area=self.__areainvestigacion,
                tipoinvestigacion=self.__tipoinvestigacion
            )
        )
        return d