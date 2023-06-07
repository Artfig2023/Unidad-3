from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoria = ''
    __importeextra = 0.0
    def __init__(self, cui:int, apel, nom, sueb:float, anti:int, carr, carg, cate, areai, tipoi, categ, impex):
        super().__init__(cui, apel, nom, sueb, anti, carr, carg, cate)
        Investigador.__init__(cui, apel, nom, sueb, anti, areai, tipoi)
        self.__categoria = categ
        self.__importeextra = impex

    def getcategoria(self): return self.__categoria
    def getimporte(self): return self.__importeextra

    def __str__(self):
        return super().__str__() + ' /Categoria: ' + self.__categoria + ' /Importe Extra: $' + self.__importeextra

    def calculaSueldo(self):
        total = Docente.calculaSueldo(self) + self.__importeextra
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
                carrera=super().getcarrera(),
                cargo=super().getcargo(),
                catedra=super().getcatedra(),
                area=super().getarea(),
                tipoinvestigacion=super().gettipo(),
                categoriaincentivos=self.__categoria,
                importeextra=self.__importeextra
            )
        )
        return d