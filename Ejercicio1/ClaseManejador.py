import csv
from ClaseFacultad import Facultad

class Manejador:

    def __init__(self):
        self.__listafacultades = []

    def agregafacultad(self, facu:Facultad):
        self.__listafacultades.append(facu)

    def testfacultad(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo,delimiter=';')
        band = True
        auxcarr = []
        auxfacu = next(reader)
        while(band):
            linea = next(reader)
            while band and auxfacu[0] == linea[0]:
                auxcarr.append(linea)
                try:
                    linea = next(reader)
                except:
                    band = False
            unafacultad = Facultad(int(auxfacu[0]), auxfacu[1], auxfacu[2], auxfacu[3], auxfacu[4], auxcarr)
            self.agregafacultad(unafacultad)
            auxcarr.clear()
            auxfacu = linea
        archivo.close()

    def buscafacultad(self, cod):
        i = 0
        band = -1
        while i < len(self.__listafacultades) and band == -1:
            if self.__listafacultades[i].getcodigo() == cod:
                band = i
            else:
                i += 1
        return band

    def muestrafacu(self, indice):
        print('Facultad: {}'.format(self.__listafacultades[indice].getnombre()))
        print('Carreras...')
        lista = self.__listafacultades[indice].getcarreras()
        for i in range(len(lista)):
            print(lista[i])

    def muestracarrera(self, nomb):
        i = 0
        j = 0
        band = False
        while i < len(self.__listafacultades) and band == False:
            carreras = self.__listafacultades[i].getcarreras()
            while j < len(carreras) and band == False:
                if nomb.lower() in carreras[j].getnombre().lower():
                    print('Informacion... ')
                    print('Codigo: {} {}'.format(self.__listafacultades[i].getcodigo(), carreras[j].getcodigo()))
                    print('Nombre: {}'.format(carreras[j].getnomb()))
                    print('Localidad: {}'.format(self.__listafacultades[i].getlocalidad()))
                    band = True
                else:
                    j += 1
            i += 1
            j = 0
        return band