from zope.interface import implementer
from Interfaces import Iinterface
from ClassLista import Lista
from ClaseDocente import Docente
from ClasePersonalApoyo import PersonalApoyo
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador

@implementer(Iinterface)

class Manejador:
    __listagentes = None

    def __init__(self):
        self.__listagentes = Lista()

    def agregar(self, unagente):
        self.__listagentes.agregagente(unagente)
        print('Agente agregado')

    def cargaDocente(self):
        print('Cargar Docente: ')
        cuil = input('Ingrese CUIL:')
        apellido = input('Ingrese apellido:')
        nombre = input('Ingrese nombre:')
        band = False
        while not band:
            try:
                sueldo = float(input('Ingrese sueldo base: '))
                assert type(sueldo) is float, 'Debe ser un numero real'
                assert sueldo > 0, 'Debe ser un numero positivo mayor que 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        band = False
        while not band:
            try:
                antiguedad = int(input('Ingrese antiguedad: '))
                assert type(antiguedad) is int, 'Debe ser un numero entero'
                assert antiguedad > 0, 'Debe ser un numero positivo mayor que 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        carrera = input('Ingrese Carrera: ')
        band = False
        while not band:
            try:
                cargo = input('Ingrese cargo (simple, semiexclusivo, exclusivo): ')
                cargo = cargo.lower()
                assert cargo == 'simple' or cargo == 'semiexclusivo' or cargo == 'exclusivo', 'Debe ingresar una opcion citada'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band == True
        catedra = input('Ingrese catedra: ')
        undocente = Docente(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra)
        return undocente

    def cargapoyo(self):
        print('Cargar Personal de Apoyo: ')
        cuil = input('Ingrese CUIL:')
        apellido = input('Ingrese apellido:')
        nombre = input('Ingrese nombre:')
        band = False
        while not band:
            try:
                sueldo = float(input('Ingrese sueldo base: '))
                assert type(sueldo) is float, 'Debe ser un numero real'
                assert sueldo > 0, 'Debe ser un numero positivo mayor que 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        band = False
        while not band:
            try:
                antiguedad = int(input('Ingrese antiguedad: '))
                assert type(antiguedad) is int, 'Debe ser un numero entero'
                assert antiguedad > 0, 'Debe ser un numero positivo mayor que 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        band = False
        while not band:
            try:
                categoria = input('Ingrese categoria (De 1 a 22): ')
                assert type(categoria) is int, 'Debe ser un numero entero'
                assert categoria >= 1 and categoria <= 22, 'Debe ser un numero entre 1 y 22'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        unapoyo = PersonalApoyo(cuil, apellido, nombre, sueldo, antiguedad, categoria)
        return unapoyo

    def cargaInvestigador(self):
        print('Cargar Investigador: ')
        cuil = input('Ingrese CUIL:')
        apellido = input('Ingrese apellido:')
        nombre = input('Ingrese nombre:')
        band = False
        while not band:
            try:
                sueldo = float(input('Ingrese sueldo base: '))
                assert type(sueldo) is float, 'Debe ser un numero real'
                assert sueldo > 0, 'Debe ser un numero positivo mayor que 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        band = False
        while not band:
            try:
                antiguedad = int(input('Ingrese antiguedad: '))
                assert type(antiguedad) is int, 'Debe ser un numero entero'
                assert antiguedad > 0, 'Debe ser un numero positivo mayor que 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        area = input('Ingrese area de investigacion (Exactas, Sociales, Naturales, etc...): ')
        tipoinv = input('Ingrese tipo de investigacion (Experimental, Descripta, etc...):')
        uninvestigacion = Investigador(cuil, apellido, nombre, sueldo, antiguedad, area, tipoinv)
        return uninvestigacion

    def cargadocenteinvestigador(self):
        print('Cargar Docente Investigador: ')
        cuil = input('Ingrese CUIL:')
        apellido = input('Ingrese apellido:')
        nombre = input('Ingrese nombre:')
        band = False
        while not band:
            try:
                sueldo = float(input('Ingrese sueldo base: '))
                assert type(sueldo) is float, 'Debe ser un numero real'
                assert sueldo > 0, 'Debe ser un numero positivo mayor que 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        band = False
        while not band:
            try:
                antiguedad = int(input('Ingrese antiguedad: '))
                assert type(antiguedad) is int, 'Debe ser un numero entero'
                assert antiguedad > 0, 'Debe ser un numero positivo mayor que 0'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        carrera = input('Ingrese Carrera: ')
        band = False
        while not band:
            try:
                cargo = input('Ingrese cargo (simple, semiexclusivo, exclusivo): ')
                cargo = cargo.lower()
                assert cargo == 'simple' or cargo == 'semiexclusivo' or cargo == 'exclusivo', 'Debe ingresar una opcion citada'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band == True
        catedra = input('Ingrese catedra: ')
        area = input('Ingrese area de investigacion (Exactas, Sociales, Naturales, etc...): ')
        tipoinv = input('Ingrese tipo de investigacion (Experimental, Descripta, etc...):')
        band = False
        while not band:
            try:
                categoriaincentivo = input('Ingrese categoria de incentivos (I, I, II, IV, V): ')
                categoriaincentivo = categoriaincentivo.upper()
                assert len(categoriaincentivo) <= 3, 'Solo se permiten 3 caracteres'
                assert categoriaincentivo == 'I' or categoriaincentivo == 'II' or categoriaincentivo == 'III' or categoriaincentivo == 'IV' or categoriaincentivo == 'V'
            except:
                print('Error. Ingrese un elemento valido')
            else:
                band = True
        ban = False
        while not ban:
            try:
                impextra = float(input('Ingrese importe extra por docencia e investigacion (numero entero o decimal):'))
                assert type(impextra) is float, "Debe ser un numero entero o decimal."
                assert impextra > 0, "Debe ser un numero positivo (mayor a cero)."
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                ban = True
        undocenteinvestigador = DocenteInvestigador(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo,
                                                    catedra, area, tipoinv, categoriaincentivo, impextra)
        return undocenteinvestigador

    def cargaunagente(self):
        print('Cargar Agente: ')
        print('1- Docente /2- Personal de Apoyo /3- Investigador /4- Docente Investigador')
        band = False
        while not band:
            try:
                opcion = int(input('Ingrese opcion: '))
                assert type(opcion) is int, 'Debe ingresar un numero entero'
                assert opcion >= 1 and opcion <= 4, 'Debe ingresar un numero de opcion valido'
            except:
                print('Error. Reintente introducir un valor valido.')
            else:
                band == True
        if opcion == 1:
            unagente = self.cargaDocente()
            print('Se cargo un Docente')
        elif opcion == 2:
            unagente = self.cargapoyo()
            print('Se cargo un Personal de Apoyo')
        elif opcion == 3:
            unagente = self.cargaInvestigador()
            print('Se cargo un Investigador')
        elif opcion == 4:
            unagente = self.cargadocenteinvestigador()
            print('Se cargo un Docente Investigador')
        return unagente

    @implementer(Iinterface)
    def insertarElemento(self, elem, xpos):
        self.__listagentes.insertaagente(elem, xpos)

    @implementer(Iinterface)
    def agregarElemento(self, elem):
        self.__listagentes.agregagente(elem)

    @implementer(Iinterface)
    def mostrarElemento(self, xpos):
        agente = self.__listagentes.buscaposicion(xpos)
        if agente.__class__.__name__ == 'Docente':
            print('En la posicion {} hay un Docente'.format(xpos + 1))
        elif agente.__class__.__name__ == 'PersonalApoyo':
            print('En la posicion {} hay un Personal de Apoyo'.format(xpos + 1))
        elif agente.__class__.__name__ == 'Investigador':
            print('En la posicion {} hay un Investigador'.format(xpos + 1))
        elif agente.__class__.__name__ == 'DocenteInvestigador':
            print('En la posicion {} hay un Docente Investigador'.format(xpos + 1))
        else:
            print('No hay agentes registrados en la posicion {}', xpos + 1)

    def ordenarpornombre(self, listado):
        listado.sort(reverse=True)
        return listado

    def listardocentesinvestgador(self, carrera):
        lista = []
        for agente in self.__listagentes:
            if isinstance(agente, DocenteInvestigador):
                if agente.getcarrera().lower() == carrera:
                    lista.append(agente)
        lista = self.ordenarpornombre(lista)
        print('Nombre   Apellido      CUIL        Area de investigacion')
        for i in range(len(lista)):
            print('%s   %s  %s\t\t%s' % (
            lista[i].getnombre(), lista[i].getapellido(), lista[i].getcuil(), lista[i].getarea()))

    def contararea(self, area):
        cont = [0,0]
        for agente in self.__listagentes:
            if isinstance(agente, DocenteInvestigador):
                if agente.getarea().lower() == area:
                    cont[0] += 1
            elif isinstance(agente, Investigador):
                if agente.getarea().lower() == area:
                    cont[1] += 1
        print('Area: {}', area)
        print('Total de Investigadores: {}', cont[1])
        print('Total de Docentes Investigadores: {}', cont[0])

    def listartodosagentes(self):
        lista = []
        for agente in self.__listagentes:
            lista.append()
        lista = self.ordenarpornombre(lista)
        print('Nombre   Apellido    Tipo de Agente     Sueldo')
        for i in range(len(lista)):
            if isinstance(lista[i], Docente):
                tipoagente = 'Docente'
            elif isinstance(lista[i], PersonalApoyo):
                tipoagente = 'PersonalApoyo'
            elif isinstance(lista[i], Investigador):
                tipoagente = 'Investigador'
            elif isinstance((lista[i], DocenteInvestigador)):
                tipoagente = 'DocenteInvestigador'
            print('%s   %s  \t %s \t\t\t %.2f' % (
            lista[i].getNombre(), lista[i].getApellido(), tipoagente, lista[i].calculaSueldo()))

    def mostrardocentes(self, categ):
        total = 0
        print('Listado de Docentes Investigadores con categoria {}: ',format(categ))
        print('Apellido    Nombre   Importe')
        for agente in self.__listagentes:
            if isinstance(agente, DocenteInvestigador):
                print('%s   %s  \t%.2f' % (agente.getApellido(), agente.getNombre(), agente.getimporte()))
                total += agente.getimporte()
        print('------------------------------------------ -> Total a pagar: ${}', total)

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            agentes=[agente.toJSON() for agente in self.__listagentes]
        )
        return d