from ClaseAgente import Agente

class PersonalApoyo(Agente):
    __categoria = ''
    def __init__(self, cui:int, apel, nom, sueb:float, anti:int, catego):
        super().__init__(cui, apel, nom, sueb, anti)
        self.__categoria = catego

    def getcategoria(self): return self.__categoria

    def __str__(self):
        return super().__str__() + ' /Categoria: ' + self.__categoria

    def calculaSueldo(self):
        porcen_antig = ((super().getSueldoBasico() * super().getAntiguedad()) / 100)
        porcen_categ = 0
        if self.__categoria >= 1 and self.__categoria <= 10:
            porcen_categ = ((super().getSueldoBasico() * 10) / 100)
        elif self.__categoria >= 11 and self.__categoria <= 20:
            porcen_categ = ((super().getSueldoBasico() * 20) / 100)
        elif self.__categoria >= 21 and self.__categoria <= 22:
            porcen_categ = ((super().getSueldoBasico() * 30) / 100)
        total = super().getSueldoBasico() + porcen_antig + porcen_categ
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
                categoria=self.__categoria
            )
        )
        return d