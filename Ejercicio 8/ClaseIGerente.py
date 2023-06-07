from zope.interface import Interface

class IGerente(Interface):
    def modificarBasicoEPlanta(dni, nuevobasico):
        pass
    def modificarViaticoEExterno(dni, nuevoviatico):
        pass
    def modificarValorEPorHora(dni, nuevovalorhora):
        pass