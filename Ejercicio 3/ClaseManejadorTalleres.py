from ClaseTaller import Taller
import csv
class ManejoTalleres:

    def __init__(self):
        self.__listatalleres = []

    def testtalleres(self):
        archivo = open('Talleres.csv')
        reader = csv.reader(archivo,delimiter=';')
        band = True
        for fila in reader:
            if band:
                self.__listatalleres.index(fila[0])
                band = not band
            else:
                untaller = Taller(fila[0], fila[1], fila[2], fila[3])
                self.__listatalleres.append(untaller)
        print('Datos de talleres cargados')

    def buscataller(self, nomb):
        i = 0
        taller = None
        while i < len(self.__listatalleres) and self.__listatalleres[i].getnombre().lower() != nomb.lower():
            i += 1

        if i < len(self.__listatalleres):
            taller = self.__listatalleres[i]

        return taller