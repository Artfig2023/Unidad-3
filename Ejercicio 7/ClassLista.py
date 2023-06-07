from ClaseNodo import Nodo

class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    __cantnodos = 0

    def __init__(self):
        self.__comienzo = None
        self.__siguiente = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getdato()
            self.__actual = self.__actual.getsiguiente()
            return dato

    def agregagente(self, unagente):
        nodo = Nodo(unagente, self.__cantnodos)
        self.__cantnodos += 1
        nodo.setsiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertaagente(self, unagente, xpos):
        band = False
        aux = self.__comienzo
        anterior = aux
        if xpos < self.__tope:
            while aux != None and band == False:
                if aux.getposicion() == xpos:
                    nodo = Nodo(unagente, xpos)
                    anterior.setsiguiente(aux)
                    band = True
                    self.__tope += 1
                    print('Agente Insertado')
                else:
                    anterior = aux
                    aux = aux.getsiguiente()
        else:
            print('El numero de posicion supera la cantidad de elementos de la lista')

    def buscaposicion(self, xpos):
        aux = self.__comienzo
        band = False
        dato = None
        while aux != None and band == False:
            if aux.getposicion() == xpos:
                dato = aux.getdato()
                band = True
            else:
                aux = aux.getsiguiente()
        return dato